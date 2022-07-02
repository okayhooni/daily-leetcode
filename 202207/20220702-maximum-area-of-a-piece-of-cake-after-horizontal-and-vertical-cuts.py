"""
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

> Topic: Math / Greedy Algorithm / Sorting

Hint)
- Sort the arrays,
  then compute the maximum difference between two consecutive elements for horizontal cuts and vertical cuts.
- The answer is the product of these maximum values in horizontal cuts and vertical cuts.

Ref) https://dev.to/seanpgallivan/solution-maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts-45p8
"""
from typing import *
from itertools import chain


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        prev_horizon = prev_vertical = 0
        max_height = max_width = 0
        horizontalCuts.sort()
        verticalCuts.sort()

        for cur_horizon in chain(horizontalCuts, [h]):
            max_height = max(max_height, cur_horizon - prev_horizon)
            prev_horizon = cur_horizon

        for cur_vertical in chain(verticalCuts, [w]):
            max_width = max(max_width, cur_vertical - prev_vertical)
            prev_vertical = cur_vertical

        return max_height * max_width % (10 ** 9 + 7)


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]) == 4
