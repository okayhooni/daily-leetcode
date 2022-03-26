"""
https://leetcode.com/problems/binary-search
"""
from typing import List
from bisect import bisect_left


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(log(n))
    공간 복잡도: O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1

    def search_with_recursion(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int):
            if left > right:
                return -1

            mid = (left + right) // 2
            if nums[mid] < target:
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return mid

        return binary_search(0, len(nums) - 1)

    def search_with_bisect_module(self, nums: List[int], target: int) -> int:
        insert_idx = bisect_left(nums, target)

        if insert_idx < len(nums) and nums[insert_idx] == target:
            return insert_idx
        else:
            return -1
