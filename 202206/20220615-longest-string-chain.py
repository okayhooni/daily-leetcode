"""
https://leetcode.com/problems/longest-string-chain/

> Topic: Dynamic Programming / Hash Table (Set/Dict)

Ref)
- https://dev.to/seanpgallivan/solution-longest-string-chain-3k9l
- https://blog.devgenius.io/google-interview-problem-longest-string-chain-5da51dd6bd4

Hint 1) Instead of adding a character, try deleting a character to form a chain in reverse.
[just consider the index position of "deleted" character,
instead of the index position of "adding" character and what the "adding" character is]

while a word may have many 26 * (word.length + 1) possible successors, it can only have word.length predecessors.
So rather than iterating from small to large words and checking every combination for a link,
we can store the words in a set and only check the few possible predecessors while iterating from large to small.

Hint 2) For each word in order of length, for each word2 which is word with one character removed,
length[word2] = max(length[word2], length[word] + 1).

we can use a dynamic programming (DP) approach to eliminate some common subproblems.
We can define a hashmap (dp) where dp[word] is the length of the longest chain ending at word found so far.
"""
from typing import List
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        Time Complexity: O(N*M) where N is the length of words and M is the average length of the words in words.
        (Extra) Space Complexity: O(N + P) where P is the number of predecessors found and stored in dp.
        """
        map_len_to_words = defaultdict(list)
        dp = {}
        ans = 1

        min_len = float('inf')
        max_len = 0
        for w in words:
            cur_word_len = len(w)
            map_len_to_words[cur_word_len].append(w)
            min_len = min(min_len, cur_word_len)
            max_len = max(max_len, cur_word_len)
            dp[w] = 1

        for cur_word_len in range(max_len, min_len - 1,  -1):
            if cur_word_len not in map_len_to_words or cur_word_len - 1 not in map_len_to_words:
                continue

            for cur_word in map_len_to_words[cur_word_len]:
                for removed_char_idx in range(cur_word_len):
                    sub_word: str = cur_word[:removed_char_idx] + cur_word[removed_char_idx + 1:]
                    if sub_word not in dp:
                        continue

                    dp[sub_word] = max(dp[sub_word], dp[cur_word] + 1)
                    # print(sub_word, dp)
                    ans = max(ans, dp[sub_word])

        return ans

    def longestStrChainRef(self, words: List[str]) -> int:
        """
        1 <= words[i].length <= 16
        """
        W = [set() for _ in range(17)]
        for word in words:
            W[len(word)].add(word)
        dp, best = defaultdict(lambda: 1), 1
        for i in range(16, 0, -1):
            if len(W[i - 1]) == 0: continue
            for word in W[i]:
                wVal = dp[word]
                for j in range(len(word)):
                    pred = word[0:j] + word[j + 1:]
                    if pred in W[i - 1] and wVal >= (dp.get(pred) or 1):
                        dp[pred] = wVal + 1
                        best = max(best, wVal + 1)
        return best


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
    print(sol.longestStrChain(["abcd", "dbqca"]))
