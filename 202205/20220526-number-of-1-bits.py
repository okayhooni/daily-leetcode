"""
https://leetcode.com/problems/number-of-1-bits/

> Topic: Bit Manipulation
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    def hammingWeightBitwise(self, n: int) -> int:
        count = 0

        while n > 0:
            # print(n, bin(n))
            count += (n % 2 != 0)
            n = n >> 1

        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingWeight(100))
    print(sol.hammingWeightBitwise(100))
