"""
https://leetcode.com/problems/triangle/

> Topic: Dynamic Programming
> Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
from typing import List
from functools import cache
from math import inf


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        > Follow up:
        Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?

        forward: (0, 1) -> 0 / (1, 2) -> 1 / (2, 3) -> 2    [|\]
        backward: (4, 5) -> 5 / (3, 4) -> 4 / (2, 3) -> 3   [/|]
        """
        dp = [val for val in triangle[-1]]
        # print(dp)
        for row_idx in range(len(triangle) - 2, -1, -1):
            for col_idx in range(len(triangle[row_idx])):
                dp[col_idx] = triangle[row_idx][col_idx] + min(dp[col_idx], dp[col_idx + 1])
            # print(row_idx, dp)

        return dp[0]

    def minimumTotalWithArgSpaceTrickDP(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            # for j in range(len(triangle[i]) - 1, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    def minimumTotalWithDP(self, triangle: List[List[int]]) -> int:
        max_row_idx = len(triangle) - 1

        @cache
        def dfs(row_idx: int, col_idx: int) -> int:
            cur_val = triangle[row_idx][col_idx]

            if row_idx == max_row_idx:
                return cur_val

            return cur_val + min(
                dfs(row_idx + 1, col_idx),
                dfs(row_idx + 1, col_idx + 1),
            )

        return dfs(0, 0)

    def minimumTotalNaiveDfs(self, triangle: List[List[int]]) -> int:
        """
        Time Limit Exceeded
        """
        min_total = inf
        max_row_idx = len(triangle) - 1

        def dfs(row_idx: int, col_idx: int, accumulated_sum: int):
            nonlocal min_total

            accumulated_sum += triangle[row_idx][col_idx]

            if row_idx == max_row_idx:
                min_total = min(min_total, accumulated_sum)
                return

            dfs(row_idx + 1, col_idx, accumulated_sum)
            dfs(row_idx + 1, col_idx + 1, accumulated_sum)

        dfs(0, 0, 0)
        return min_total


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
