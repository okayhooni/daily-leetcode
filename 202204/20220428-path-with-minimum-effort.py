"""
https://leetcode.com/problems/path-with-minimum-effort/

> Consider the grid as a graph, where adjacent cells have an edge with cost of the difference between the cells.
"""
from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)]  # (effort, row, col)

        height = len(heights)
        width = len(heights[0])

        visited = set()  # (row, col)

        while heap:
            cur_effort, cur_row, cur_col = heapq.heappop(heap)

            if cur_row == height - 1 and cur_col == width - 1:
                return cur_effort

            if (cur_row, cur_col) in visited:
                continue

            visited.add((cur_row, cur_col))

            if cur_row + 1 < height:
                delta = abs(heights[cur_row + 1][cur_col] - heights[cur_row][cur_col])
                heapq.heappush(heap, (max(cur_effort, delta), cur_row + 1, cur_col))
            if 0 <= cur_row - 1:
                delta = abs(heights[cur_row - 1][cur_col] - heights[cur_row][cur_col])
                heapq.heappush(heap, (max(cur_effort, delta), cur_row - 1, cur_col))
            if cur_col + 1 < width:
                delta = abs(heights[cur_row][cur_col + 1] - heights[cur_row][cur_col])
                heapq.heappush(heap, (max(cur_effort, delta), cur_row, cur_col + 1))
            if 0 <= cur_col - 1:
                delta = abs(heights[cur_row][cur_col - 1] - heights[cur_row][cur_col])
                heapq.heappush(heap, (max(cur_effort, delta), cur_row, cur_col - 1))

        return -1
