"""
https://leetcode.com/problems/short-encoding-of-words/

> Topic: Trie / Hash Table (Set/Dict) / String

Ref)
- https://dev.to/seanpgallivan/solution-short-encoding-of-words-39g0
- https://dev.to/seanpgallivan/solution-short-encoding-of-words-ver-2-423i
- https://github.com/azl397985856/leetcode/blob/master/problems/820.short-encoding-of-words.md

When you build out a trie,
you iterate through the granular segments of the data and go down existing branches of the trie,
when they exist and create them when they don't.

For this problem, the entries are words and thus the granular segments are characters.
We'll also be iterating through the characters in reverse order, since we're dealing with suffixes instead of prefixes.

We could fully build out the trie then later traverse the trie to calculate our answer (ans),
but instead we can just keep our ans up-to-date as we build out the trie to be more efficient.

As we build out our trie, there are three things we have to look out for:

1) If any new branches are formed while processing a word, then that word must be new and we should add its length
(plus 1 for the '#' at the end) to our ans.

2) If a word ends without forging a new branch, then it must be the suffix of an earlier word,
so we shouldn't add its length to our ans.

3) If there are no other branches on the node in which the first new branch is formed while processing a word,
then some earlier word must be a suffix to the current word, so we should subtract the already added amount from our ans.

The third check in particular will allow us to avoid needing to sort W before entry.
In order to prevent the third check from triggering every time a word extends into new territory
(which would happen with each new character), we can use a boolean flag (newWord) to mark only the first instance.
"""
from typing import List, Dict
from dataclasses import dataclass, field


@dataclass
class TrieNode:
    char: str = None
    next_nodes_by_char: Dict[str, "TrieNode"] = field(default_factory=dict)

    def __len__(self):
        return len(self.next_nodes_by_char)


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        wset = set(words)
        for word in words:
            if word in wset:
                for i in range(1, len(word)):
                    wset.discard(word[i:])
        return len("#".join(list(wset))) + 1

    def minimumLengthEncodingWithTrie(self, words: List[str]) -> int:
        reverse_trie_root = TrieNode()
        ans = 0  # 1
        for word in words:
            cur_node = reverse_trie_root
            is_new_word = False
            for char_idx, char in enumerate(reversed(word), 1):
                # if not cur_node and not is_new_word:
                if not cur_node and not is_new_word and cur_node is not reverse_trie_root:
                    ans -= char_idx
                if char not in cur_node.next_nodes_by_char:
                    is_new_word = True
                    cur_node.next_nodes_by_char[char] = TrieNode(char)

                cur_node = cur_node.next_nodes_by_char[char]

            if is_new_word:
                ans += len(word) + 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumLengthEncodingWithTrie(["time", "me", "bell"]))
