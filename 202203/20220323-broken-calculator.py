"""
https://leetcode.com/problems/broken-calculator/
"""


class Solution:
    """
    시간 복잡도: O(n)
    공간 복잡도: O(1)
    """
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while startValue < target:
            ans += 1
            if target % 2:
                target += 1
            else:
                target /= 2

        return int(ans + startValue - target)
