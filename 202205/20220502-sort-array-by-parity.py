"""
https://leetcode.com/problems/sort-array-by-parity/
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(n)
        """
        even_nums, odd_nums = [], []

        for n in nums:
            if n % 2:
                odd_nums.append(n)
            else:
                even_nums.append(n)

        return even_nums + odd_nums

    def sortArrayByParity62msSol(self, nums: List[int]) -> List[int]:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(1)
        """
        if len(nums) == 1:
            return nums
        index = 0

        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                continue
            nums[index], nums[i] = nums[i], nums[index]
            index += 1

        return nums
