"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

> Topic: Math / Sorting

Ref) https://dev.to/seanpgallivan/solution-minimum-moves-to-equal-array-elements-ii-oej

Let's consider a possible scenario,
in which we've decided that our target value is x which would take ans number of moves to complete.

What would happen to ans if we increased x by 1?
If we did, each element that is below the new x would have to spend another move to get up to x,
but every element that is above the new x would have to spend one less move to get down to x.
This means that x should naturally move up if there are more elements above x than below.

It also means the inverse, that x should move down if there are more elements below x than above.
The natural outcome of this is that x will settle at a spot where there are the same number of elements on either side,
which is the median value of nums.

To find the median value, we'll have to first sort nums.
If nums has an even number of elements, any value between the two middle elements, inclusive,
will work for calculating the answer, so we don't have to worry about which of the two elements we use for our solution.
"""
from typing import *
from statistics import median


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N * log N) where N is the length of nums, for sorting nums
        Space Complexity: O(1)
        """
        med = round(median(nums))
        ans_moves = 0

        for n in nums:
            ans_moves += abs(med - n)

        return ans_moves


if __name__ == "__main__":
    sol = Solution()
    assert sol.minMoves2([1, 10, 2, 9]) == 16
    assert sol.minMoves2([1, 0, 0, 8, 6]) == 14
