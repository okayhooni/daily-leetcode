"""
https://leetcode.com/problems/network-delay-time/
"""
from typing import List
from collections import defaultdict
from heapq import heappush, heappop

INF = float('inf')


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        networks = defaultdict(list)
        for u, v, w in times:
            networks[u - 1].append((v - 1, w))

        cost = [INF for _ in range(n)]
        visited = [False for _ in range(n)]
        heap_queue = []
        cur_node_idx = k - 1
        cost[cur_node_idx] = 0
        heappush(heap_queue, (cost[cur_node_idx], cur_node_idx))
        while heap_queue:
            cur_min_time_cost, cur_node_idx = heappop(heap_queue)
            visited[cur_node_idx] = True
            for neighbor_idx, weight in networks[cur_node_idx]:
                # if not visited[neighbor_idx]:  # WRONG
                if cost[neighbor_idx] > cur_min_time_cost + weight:
                # if not visited[neighbor_idx] and cost[neighbor_idx] > cur_min_time_cost + weight:
                    cost[neighbor_idx] = cur_min_time_cost + weight
                    heappush(heap_queue, (cost[neighbor_idx], neighbor_idx))

        if not all(visited):
            return -1

        return int(max(cost))

    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        networks = defaultdict(list)
        for u, v, w in times:
            networks[u - 1].append((v - 1, w))

        cost = [INF for _ in range(n)]
        visited = [False for _ in range(n)]
        heap_queue = []
        cur_node_idx = k - 1
        cost[cur_node_idx] = 0
        heappush(heap_queue, (cost[cur_node_idx], cur_node_idx))
        while heap_queue:
            cur_min_time_cost, cur_node_idx = heappop(heap_queue)

            if visited[cur_node_idx]:
                continue

            visited[cur_node_idx] = True
            cost[cur_node_idx] = cur_min_time_cost
            for neighbor_idx, weight in networks[cur_node_idx]:
                heappush(heap_queue, (cur_min_time_cost + weight, neighbor_idx))

        if not all(visited):
            return -1

        return int(max(cost))

    def networkDelayTime3(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        heap_queue = [(0, k)]
        cost = {}

        while heap_queue:
            time_cost, node = heappop(heap_queue)
            if node not in cost:  # NOT VISITED
                cost[node] = time_cost
                for v, w in graph[node]:
                    alt = time_cost + w
                    # if v not in cost:
                    #     heappush(heap_queue, (alt, v))  # OK!
                    heappush(heap_queue, (alt, v))

        if len(cost) == n:
            return max(cost.values())
        return -1
