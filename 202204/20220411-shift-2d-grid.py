"""
https://leetcode.com/problems/shift-2d-grid/
"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        width, height = len(grid[0]), len(grid)

        res = [[0 for _ in range(width)] for _ in range(height)]

        for prev_vertical_jdx in range(height):
            for prev_horizontal_idx in range(width):

                vertical_jumps, new_horizontal_idx = divmod(prev_horizontal_idx + k, width)
                new_vertical_jdx = (prev_vertical_jdx + vertical_jumps) % height

                res[new_vertical_jdx][new_horizontal_idx] = grid[prev_vertical_jdx][prev_horizontal_idx]

        return res

    def shiftGrid_152ms_sol(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        k %= (m * n)

        flat = tuple(grid[i][j] for i in range(m) for j in range(n))

        flat = flat[-k:] + flat[:-k]

        ans = [[flat[i * n + j] for j in range(n)] for i in range(m)]

        return ans
