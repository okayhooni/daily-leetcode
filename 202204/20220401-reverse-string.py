"""
https://leetcode.com/problems/reverse-string/
"""
from typing import List


class Solution:
    """
    Do not return anything, modify s in-place instead.
    """
    def reverseString(self, s: List[str]) -> None:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(1)
        """
        s.reverse()

    def reverseStringTwoPointer(self, s: List[str]) -> None:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(1)
        """

        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
