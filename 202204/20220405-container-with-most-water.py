"""
https://leetcode.com/problems/container-with-most-water/

cf) https://leetcode.com/problems/trapping-rain-water/
"""

from typing import List


class Solution:
    """
    시간 복잡도: O(n)
    공간 복잡도: O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        max_area_value = 0

        while left < right:
            cur_area_value = (right - left) * min(height[left], height[right])
            max_area_value = max(max_area_value, cur_area_value)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area_value
