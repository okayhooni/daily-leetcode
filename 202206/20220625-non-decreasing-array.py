"""
https://leetcode.com/problems/non-decreasing-array/

> Topic: Array / Math

Ref) https://dev.to/seanpgallivan/solution-non-decreasing-array-1m5c
"""
from typing import *


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(N) where N is the length of N
        (Extra) Space Complexity: O(1) with no modification of inputs
        """
        has_decreasing_case = False
        for prev_idx in range(len(nums) - 1):
            prev, cur = nums[prev_idx:prev_idx+2]
            if prev > cur:
                if has_decreasing_case:
                    return False
                if 1 <= prev_idx < len(nums) - 2 and prev > nums[prev_idx+2] and nums[prev_idx-1] > cur:
                    return False

                has_decreasing_case = True

        return True

    def checkPossibilityRef(self, nums: List[int]) -> bool:
        err = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if err or (i > 1 and i < len(nums) - 1 and nums[i - 2] > nums[i] and nums[i + 1] < nums[i - 1]):
                    return False
                err = 1
        return True


if __name__ == '__main__':
    sol = Solution()
    # assert sol.checkPossibility([4, 2, 3])
    # assert not sol.checkPossibility([4, 2, 1])
    assert not sol.checkPossibility([3, 4, 2, 3])
    assert sol.checkPossibility([5, 7, 1, 8])
    assert sol.checkPossibility([1])
