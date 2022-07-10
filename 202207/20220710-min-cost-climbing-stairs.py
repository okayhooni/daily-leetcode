"""
https://leetcode.com/problems/min-cost-climbing-stairs/

> Topic: Dynamic Programming

Hint) Say f[i] is the final cost to climb to the top from step i. Then f[i] = cost[i] + min(f[i+1], f[i+2]).

Ref) https://dev.to/seanpgallivan/solution-min-cost-climbing-stairs-5ak9
"""
from typing import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        it = iter(cost)
        prev_prev = next(it)
        prev = next(it)
        for cur_cost in it:
            prev_prev, prev = prev, cur_cost + min(prev_prev, prev)

        return min(prev_prev, prev)


if __name__ == '__main__':
    sol = Solution()
    assert sol.minCostClimbingStairs([10, 15, 20]) == 15
    assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
