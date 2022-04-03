"""
https://leetcode.com/problems/next-permutation

The replacement must be in place and use only constant extra memory.
Do not return anything, modify nums in-place instead.
"""
from typing import List


class Solution:
    """
    시간 복잡도: O(n)
    공간 복잡도: O(1)
    """
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return

        for idx in range(len(nums) - 1, 0, -1):
            if nums[idx - 1] < nums[idx]:
                start_descending_idx_on_left_direction = idx - 1
                break
        else:
            nums.reverse()
            return

        # print('start_descending_idx_on_left_direction:', start_descending_idx_on_left_direction)

        for jdx in range(start_descending_idx_on_left_direction + 1, len(nums)):
            if nums[start_descending_idx_on_left_direction] >= nums[jdx]:
                pivot_idx = jdx - 1
                break
        else:
            pivot_idx = len(nums) - 1

        # print('pivot_idx:', pivot_idx)

        nums[start_descending_idx_on_left_direction], nums[pivot_idx] = \
            nums[pivot_idx], nums[start_descending_idx_on_left_direction]

        left, right = start_descending_idx_on_left_direction + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    # l = [2, 3, 1]
    l = [1, 5, 1]
    sol = Solution()
    sol.nextPermutation(l)
    print(l)

"""
[2, 3, 4, 5] -> [2, 3, 5, 4]

[1, 3, 2]

[4, 3, 2, 1] -> [4, 3, 1, 2] -> [4, 1, 3, 2] -> [1, 4, 3, 2]



[2, 3, 5, 4] -> [2, 4, 3, 5]
[2, 3, 5, 6, 4] -> [2, 3, 6, 4, 5]
[2, 3, 4, 5] -> [2, 3, 5, 4]

[4, 5, 3] -> [5, 3, 4]
[4, 3, 5]
[3, 4, 5]
"""