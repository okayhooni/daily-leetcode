"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

> Topic: Dynamic Programming

cf) https://leetcode.com/problems/number-of-islands/

Ref)
- https://dev.to/seanpgallivan/solution-longest-increasing-path-in-a-matrix-4o5f
- https://www.geeksforgeeks.org/longest-increasing-path-matrix/

Note: It is possible to use a bottom-up dynamic programming (DP) approach here as well,
but since there's no convenient fixed-point bottom location,
we'd have to use a max-heap priority queue in order to traverse M in proper bottom-up order.
That would push the time complexity to O(N * M * log(N * M)), so the memoization code is more efficient.
"""
from typing import List
from functools import lru_cache, cache  # > Python 3.9
# 3.10.2 (main, Jan 15 2022, 18:02:07) [GCC 9.3.0]


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row_len, col_len = len(matrix), len(matrix[0])

        @cache
        def dfs(row, col):
            cur_val = matrix[row][col]
            return 1 + int(max(
                (0 <= row - 1 and cur_val < matrix[row - 1][col]) and dfs(row - 1, col),
                (row + 1 < row_len and cur_val < matrix[row + 1][col]) and dfs(row + 1, col),
                (0 <= col - 1 and cur_val < matrix[row][col - 1]) and dfs(row, col - 1),
                (col + 1 < col_len and cur_val < matrix[row][col + 1]) and dfs(row, col + 1)
                # (0 <= row - 1 and cur_val > matrix[row - 1][col]) and dfs(row - 1, col),
                # (row + 1 < row_len and cur_val > matrix[row + 1][col]) and dfs(row + 1, col),
                # (0 <= col - 1 and cur_val > matrix[row][col - 1]) and dfs(row, col - 1),
                # (col + 1 < col_len and cur_val > matrix[row][col + 1]) and dfs(row, col + 1)  # BOTH OK!

            ))

        return max(
            dfs(row, col)
            for row in range(row_len)
            for col in range(col_len)
        )

    def longestIncreasingPathRef(self, M: List[List[int]]) -> int:
        ylen, xlen = len(M), len(M[0])

        @lru_cache(maxsize=None)
        def dfs(y, x):
            val = M[y][x]
            return 1 + max(
                dfs(y + 1, x) if y < ylen - 1 and val > M[y + 1][x] else 0,
                dfs(y - 1, x) if y > 0 and val > M[y - 1][x] else 0,
                dfs(y, x + 1) if x < xlen - 1 and val > M[y][x + 1] else 0,
                dfs(y, x - 1) if x > 0 and val > M[y][x - 1] else 0)

        return max(dfs(y, x) for y in range(ylen) for x in range(xlen))


if __name__ == '__main__':
    test_case = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]

    sol = Solution()
    print(sol.longestIncreasingPath(test_case))
    print(sol.longestIncreasingPathRef(test_case))
