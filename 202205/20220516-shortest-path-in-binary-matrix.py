"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/

> Do a breadth first search to find the shortest path.
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    NEIGHBORS = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        row_len, col_len = len(grid), len(grid[0])
        if row_len == col_len == 1:
            return 1

        visited = {(0, 0)}

        def is_valid_remaining_grid(i, j) -> bool:
            if (i, j) in visited:
                return False

            return 0 <= i < row_len and 0 <= j < col_len and grid[i][j] == 0

        hq = [(1, 0, 0)]  # (w, i, j)

        while hq:
            w, i, j = heappop(hq)
            # if i == row_len - 1 and j == col_len - 1:
            #     return w
            # visited.add((i, j))

            for delta_i, delta_j in self.NEIGHBORS:
                neighbor_i, neighbor_j = i + delta_i, j + delta_j
                if not is_valid_remaining_grid(neighbor_i, neighbor_j):
                    continue

                if neighbor_i == row_len - 1 and neighbor_j == col_len - 1:
                    return w + 1
                visited.add((neighbor_i, neighbor_j))

                heappush(hq, (w + 1, neighbor_i, neighbor_j))

        return -1
