"""
https://leetcode.com/problems/unique-paths-ii/

> Topic: Dynamic Programming

Hint 1) The robot can only move either down or right.
Hence any cell in the first row can only be reached from the cell left to it.
However, if any cell has an obstacle, you don't let that cell contribute to any path.
So, for the first row, the number of ways will simply be

if obstacleGrid[i][j] is not an obstacle
     obstacleGrid[i,j] = obstacleGrid[i,j - 1]
else
     obstacleGrid[i,j] = 0

You can do a similar processing for finding out the number of ways of reaching the cells in the first column.

Hint 2) For any other cell, we can find out the number of ways of reaching it,
by making use of the number of ways of reaching the cell directly above it and the cell to the left of it in the grid.
This is because these are the only two directions from which the robot can come to the current cell.

Hint 3) Since we are making use of pre-computed values along the iteration, this becomes a dynamic programming problem.

if obstacleGrid[i][j] is not an obstacle
     obstacleGrid[i,j] = obstacleGrid[i,j - 1]  + obstacleGrid[i - 1][j]
else
     obstacleGrid[i,j] = 0
"""
from typing import List
from functools import cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Memoization
        """
        row_len, col_len = len(obstacleGrid), len(obstacleGrid[0])

        @cache
        def dfs(row_idx: int, col_idx: int):
            if row_idx == row_len - 1 and col_idx == col_len - 1:
                return 1

            res = 0

            if row_idx + 1 < row_len and obstacleGrid[row_idx + 1][col_idx] == 0:
                res += dfs(row_idx + 1, col_idx)

            if col_idx + 1 < col_len and obstacleGrid[row_idx][col_idx + 1] == 0:
                res += dfs(row_idx, col_idx + 1)

            return res

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        return dfs(0, 0)

    def uniquePathsWithObstaclesTabulation(self, obstacleGrid: List[List[int]]) -> int:
        """
        Tabulation
        """
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        print(dp)

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        print(dp)
        return dp[-1][-1]

    def uniquePathsWithObstaclesTabulationInPlace(self, obstacleGrid: List[List[int]]) -> int:
        """
        Approach: This is DP approach, similar to DP submission of LC-62,
        with the change being setting the position to 0 if it's blocked.
        To avoid extra space, input grid array is being modified.
        """
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if row == 0 and col == 0:
                    continue
                elif obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                elif row == 0:
                    obstacleGrid[row][col] = int(obstacleGrid[row][col - 1] == 1)
                elif col == 0:
                    obstacleGrid[row][col] = int(obstacleGrid[row - 1][col] == 1)
                else:
                    obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
        return obstacleGrid[-1][-1]


if __name__ == '__main__':
    test_case = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(test_case))
    print(sol.uniquePathsWithObstaclesTabulation(test_case))
    print(sol.uniquePathsWithObstaclesTabulationInPlace(test_case))
