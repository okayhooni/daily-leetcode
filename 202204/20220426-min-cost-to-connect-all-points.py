"""
https://leetcode.com/problems/min-cost-to-connect-all-points/

- Connect each pair of points with a weighted edge, the weight being the manhattan distance between those points.
- The problem is now the cost of minimum spanning tree in graph with above edges.

REF: https://www.tutorialspoint.com/program-to-find-minimum-cost-to-connect-all-points-in-python
"""
from typing import List, Tuple
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap: List[Tuple[int, int]] = [(0, 0)]  # [(멘하탄 거리, 포인트 인덱스)]
        undiscovered_points_idx_set = set(range(len(points)))
        total_distance = 0

        while undiscovered_points_idx_set:
            distance, current_index = heapq.heappop(heap)
            if current_index in undiscovered_points_idx_set:
                undiscovered_points_idx_set.remove(current_index)  # discard
                total_distance += distance
                x0, y0 = points[current_index]
                for other_index in undiscovered_points_idx_set:
                    x1, y1 = points[other_index]
                    heapq.heappush(heap, (abs(x0 - x1) + abs(y0 - y1), other_index))

        # print(heap)
        return total_distance


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
