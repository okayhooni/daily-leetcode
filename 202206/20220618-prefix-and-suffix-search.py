"""
https://leetcode.com/problems/prefix-and-suffix-search/

> Topic: Trie / Design

Hint 1) For a word like "test", consider "#test", "t#test", "st#test", "est#test", "test#test".
Then if we have a query like prefix = "te", suffix = "t",
we can find it by searching for something we've inserted starting with "t#te".

Ref) https://dev.to/seanpgallivan/solution-prefix-and-suffix-search-11m5

Whenever we have to deal with searching for data using a prefix or a suffix, this naturally points to a trie solution.
A trie is a type of data structure that uses a branching tree format where the nodes represent segments of data
(usually characters) to make searching by prefix faster and easier.

The difficulty in this case is that we're searching by both prefix and suffix,
so we can create two trie structures, one for prefixes and one for suffixes (pTrie, sTrie).
Then we can iterate through words and insert() each word into the two tries.
"""
from typing import List, Dict
from pprint import pformat


class TrieNode:
    def __init__(self, word_idx: int = None, char: str = None):
        self.char = char
        self.word_idx_list = [] if word_idx is None else [word_idx]
        self.next_node_by_char: Dict[str, TrieNode] = {}

    def add_word_idx(self, word_idx):
        self.word_idx_list.append(word_idx)

    def next(self, next_char: str):
        return self.next_node_by_char[next_char]

    def __len__(self):
        return len(self.word_idx_list)

    def __repr__(self):
        return pformat({
            'char': self.char,
            # 'word_idx_list': self.word_idx_list,
            'next_nodes': self.next_node_by_char,
        })


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie_root = TrieNode()
        self.boundary_node = TrieNode()

        for w_idx, w in enumerate(words):
            self._insert_word_to_trie(w_idx, w)

    def _insert_next_char_and_return_trie_node(self, node: TrieNode, next_char: str, word_idx: int):
        if next_char not in node.next_node_by_char:
            node.next_node_by_char[next_char] = TrieNode(char=next_char)

        next_node = node.next_node_by_char[next_char]
        next_node.add_word_idx(word_idx)
        return next_node

    def _insert_word_to_trie(self, word_idx: int, word: str):
        for suffix_start_idx in range(len(word)):
            cur_trie_node = self.trie_root

            for idx in range(suffix_start_idx, len(word)):
                char = word[idx]
                cur_trie_node = self._insert_next_char_and_return_trie_node(cur_trie_node, char, word_idx)

            cur_trie_node = self._insert_next_char_and_return_trie_node(cur_trie_node, '#', word_idx)

            for char in word:
                cur_trie_node = self._insert_next_char_and_return_trie_node(cur_trie_node, char, word_idx)

    def f(self, prefix: str, suffix: str) -> int:
        cur_trie_node = self.trie_root

        for suffix_char in suffix:
            if suffix_char not in cur_trie_node.next_node_by_char:
                return -1

            cur_trie_node = cur_trie_node.next_node_by_char[suffix_char]

        if '#' not in cur_trie_node.next_node_by_char:
            return -1

        cur_trie_node = cur_trie_node.next_node_by_char['#']

        for prefix_char in prefix:
            if prefix_char not in cur_trie_node.next_node_by_char:
                return -1

            cur_trie_node = cur_trie_node.next_node_by_char[prefix_char]

        return cur_trie_node.word_idx_list[-1]


class WordFilterRef:
    """
    Time Limit Exceeded
    """
    def __init__(self, words: List[str]):
        self.pTrie = [None] * 27
        self.sTrie = [None] * 27
        for index in range(len(words)):
            self.insert(words[index], index, self.pTrie)
            self.insert(words[index][::-1], index, self.sTrie)

    def insert(self, word: str, index: int, trie: list):
        for c in word:
            cval = ord(c) - 97
            if not trie[cval]: trie[cval] = [None] * 27
            trie = trie[cval]
            if not trie[26]: trie[26] = []
            trie[26].append(index)

    def retrieve(self, word: str, trie: list) -> list:
        for c in word:
            cval = ord(c) - 97
            trie = trie[cval]
            if not trie: return []
        return trie[26]

    def f(self, pre: str, suf: str) -> int:
        pVals = self.retrieve(pre, self.pTrie)
        sVals = self.retrieve(suf[::-1], self.sTrie)
        svix, pvix = len(sVals) - 1, len(pVals) - 1
        # while ~svix and ~pvix:
        while svix >= 0 and pvix >= 0:
            sVal, pVal = sVals[svix], pVals[pvix]
            if sVal == pVal: return sVal
            if sVal > pVal: svix -= 1
            else: pvix -= 1
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
if __name__ == '__main__':
    test_case_input = [
        "bacaabccba",
        "bccbacbcba"
    ]
    #     "cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
    #     "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"
    # ]
    wf = WordFilter(test_case_input)
    wf2 = WordFilter(test_case_input)
    # print(wf.trie_root)
    # print(wf.f('ab', 'd'))
    # print(wf.f("bccbacbcba", "a"))
    # print(wf.f("ab", "abcaccbcaa"))
    # print(wf.f("a", "aa"))
    print(wf.f("bac", "cba"))
    print(wf2.f("bac", "cba"))
    # print(wf.f("cabaaba", "abaaaa"))

"""
["WordFilter","f","f","f","f","f","f","f","f","f","f"]
[[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa",
"accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],
["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],
["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]
"""
