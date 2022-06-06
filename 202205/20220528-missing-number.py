"""
https://leetcode.com/problems/missing-number/

> Topic: Math / Bit Manipulation / Sorting / Hash Table (Set)
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return (set(range(len(nums) + 1)) - set(nums)).pop()

    def missingNumberMath(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)

    def missingNumberSort(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n * log(n))
        Space Complexity: O(1)
        """
        nums.sort()
        for sorted_n, no_missing_seq_n in zip(nums, range(len(nums) + 1)):
            if sorted_n != no_missing_seq_n:
                return no_missing_seq_n

        return len(nums)

    def missingNumberBitwise(self, nums: List[int]) -> int:  # TODO: THINK MORE
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        missing = len(nums)
        print(missing, bin(missing))
        print('====================================')
        for i, num in enumerate(nums):
            print(f'i ^ num (={bin(i)} ^ {bin(num)} = {bin(i ^ num)})')
            print(f'missing ^ (i ^ num)(={bin(missing)} ^ {bin(i ^ num)} = {bin(missing ^ (i ^ num))})')
            missing ^= i ^ num
            print(bin(missing))
            print('====================================')
        return missing


if __name__ == '__main__':
    sol = Solution()
    # print(sol.missingNumberBitwise([0, 1, 3]))
    # print(sol.missingNumberBitwise([0, 1, 2, 3, 4, 5, 7]))
    print(sol.missingNumberBitwise([7, 5, 4, 3, 2, 1, 0]))
