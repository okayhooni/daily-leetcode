"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        시간 복잡도: O(1) / making set: O(n)
        공간 복잡도: O(n)
        """
        return target in set(nums)

    def search_with_binary_search(self, nums: List[int], target: int) -> bool:
        """
        시간 복잡도: O(log(n)) ~ worst: O(n)
        공간 복잡도: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[mid] < nums[right]:  # 우측 정렬 확실
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[right]:  # 좌측 정렬 확실
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # nums[mid] == nums[right]
                right -= 1  # worst case: O(n)

        return False
