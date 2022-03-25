"""
https://leetcode.com/problems/two-city-scheduling
"""
from typing import List
from itertools import chain


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        시간 복잡도: O(n*log(n))
        공간 복잡도: O(1)
        """
        costs.sort(key=lambda e: e[1] - e[0])
        total_len = len(costs)
        return sum(chain(
            (costs[i][1] for i in range(total_len // 2)),
            (costs[j][0] for j in range(total_len // 2, total_len)),
        ))
