"""
https://leetcode.com/problems/critical-connections-in-a-network/

REF: https://dev.to/seanpgallivan/solution-critical-connections-in-a-network-51g0

> Hint: Use Tarjan's algorithm.

Tarjan's Bridge-Finding Algorithm (TBFA).

TBFA is a bit like a combination of a depth-first search (DFS) approach with recursion and a union-find.

IN TBFA, we do a recursive DFS on our graph,
and for each node we keep track of the earliest node that we can circle back around to reach.

By doing this, we can identify whether a given edge is a bridge,
because the far node doesn't lead back to any other earlier node.

cf)
- https://leetcode.com/problems/smallest-string-with-swaps/
- https://leetcode.com/problems/longest-consecutive-sequence/
"""
from typing import List
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for a_idx, b_idx in connections:
            graph[a_idx].append(b_idx)
            graph[b_idx].append(a_idx)

        discovery_time, lowest_time, ans = [0] * n, [0] * n, []
        cur_time = 1

        def dfs(cur_idx: int, prev_idx: int):
            nonlocal cur_time
            print(f'# VISIT NODE WITH IDX: {cur_idx} [ADJACENT TO: {graph[cur_idx]}] ON TIME ORDER: {cur_time}')
            discovery_time[cur_idx] = lowest_time[cur_idx] = cur_time
            print(f'# - discovery_time: {discovery_time}')
            cur_time += 1

            for next_idx in graph[cur_idx]:
                print(f'>>>>> BEGIN <prev_idx: {prev_idx}> / <cur_idx: {cur_idx}> / <next_idx: {next_idx}>')

                if not discovery_time[next_idx]:  # NOT VISITED
                    dfs(next_idx, cur_idx)  # DFS - VISITING!

                # AFTER BACK-TRACKING
                if next_idx != prev_idx:
                    print(f'lowest_time[cur_idx={cur_idx}]: {lowest_time[cur_idx]} / '
                          f'lowest_time[next_idx={next_idx}]: {lowest_time[next_idx]}')
                    # we've found a loop and we should update the low value for the current node
                    lowest_time[cur_idx] = min(lowest_time[cur_idx], lowest_time[next_idx])
                    print(f'-> lowest_time[cur_idx={cur_idx}]: {lowest_time[cur_idx]}')

                print(f'@@@@@ lowest_time[next_idx={next_idx}]: {lowest_time[next_idx]}')
                print(f'@@@@@ discovery_time[cur_idx={cur_idx}]: {discovery_time[cur_idx]}')
                if lowest_time[next_idx] > discovery_time[cur_idx]:
                    # there is no looped connection, meaning that the edge between curr and next is a bridge
                    ans.append([cur_idx, next_idx])
                    print(f'$$$$$ {ans}')

                print(f'>>>>> END <prev_idx: {prev_idx}> / <cur_idx: {cur_idx}> / <next_idx: {next_idx}>')

            print(f'# LEAVE NODE WITH IDX: {cur_idx}')

        dfs(0, -1)
        print('discovery_time:', discovery_time)
        print('lowest_time:', lowest_time)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # print(sol.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
    # print(sol.criticalConnections(5, [[1, 0], [2, 0], [3, 2], [4, 2], [4, 3], [3, 0], [4, 0]]))
    # print(sol.criticalConnections(5, [[1, 0], [2, 1], [3, 2], [4, 3]]))
    # print(sol.criticalConnections(5, [[4, 0], [2, 1], [3, 2], [4, 3]]))
    print(sol.criticalConnections(5, [[4, 0], [2, 1], [3, 2], [4, 3], [1, 0]]))
    # print(sol.criticalConnections(5, [[1, 0], [2, 1], [3, 2], [4, 3], [0, 4]]))
    # print(sol.criticalConnections(7, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [0, 3], [4, 6]]))
