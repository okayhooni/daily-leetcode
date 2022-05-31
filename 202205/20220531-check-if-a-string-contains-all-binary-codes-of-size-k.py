"""
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

> Topic: Bit Manipulation, Math, Hash (set)

Hint 1) We need only to check all sub-strings of length k.
Hint 2) The number of distinct sub-strings should be exactly 2^k.
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substr_set = set()
        # all_substr_cnt = 2 ** k
        all_substr_cnt = 1 << k
        left, right = 0, k

        while right <= len(s):
            substr_set.add(int(s[left:right], 2))
            if len(substr_set) == all_substr_cnt:
                return True

            left += 1
            right += 1

        return False
