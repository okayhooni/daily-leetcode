"""
https://leetcode.com/problems/maximum-product-of-word-lengths/

> Topic: Bit Manipulation (bitset / bitmap / bitmask)

Ref) https://dev.to/seanpgallivan/solution-maximum-product-of-word-lengths-d62
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        """
        cur_max_product = 0
        # words.sort(key=lambda w: len(w), reverse=True)
        words.sort(key=len, reverse=True)

        for idx in range(len(words) - 1):
            first_word = words[idx]

            for jdx in range(idx + 1, len(words)):
                second_word = words[jdx]

                if cur_max_product >= len(first_word) * len(second_word):
                    break

                if not set(first_word) & set(second_word):
                    cur_max_product = max(cur_max_product, len(first_word) * len(second_word))

        return cur_max_product

    def maxProductBitwise(self, words: List[str]) -> int:
        """
        Time Complexity: O(N^2 + N*M) where N is the length of words and M is the average length of the words in words
        Space Complexity: O(N) for bitsets
        """
        words.sort(key=len, reverse=True)
        best, bitsets = 0, {}
        for i in range(len(words)):
            wlen, bitset = len(words[i]), 0
            if wlen * len(words[0]) < best:
                return best
            for c in words[i]:
                bitset |= 1 << ord(c) - 97  # ord('a')
            print(words[i], bin(bitset))
            if bitset not in bitsets:
                for k, v in bitsets.items():
                    if not bitset & k:
                        best = max(best, wlen * v)
                bitsets[bitset] = wlen

        print(bitsets)
        return best


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
    print(sol.maxProductBitwise(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
