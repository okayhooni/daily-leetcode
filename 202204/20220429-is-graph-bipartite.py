"""
https://leetcode.com/problems/is-graph-bipartite/
"""
from typing import List, Dict


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        is_on_a_party: Dict[int, bool] = {}
        undiscovered = set(range(len(graph)))
        stack = []
        while stack or undiscovered:
            try:
                cur_node_idx = stack.pop()
            except IndexError:
                next_node_idx = undiscovered.pop()
                stack.append(next_node_idx)
                is_on_a_party[next_node_idx] = True
                continue

            cur_neighbors_idx = graph[cur_node_idx]
            for neighbor_idx in cur_neighbors_idx:
                if neighbor_idx in undiscovered:
                    is_on_a_party[neighbor_idx] = not is_on_a_party[cur_node_idx]
                    stack.append(neighbor_idx)
                    undiscovered.remove(neighbor_idx)
                    continue

                if is_on_a_party[cur_node_idx] is is_on_a_party[neighbor_idx]:
                    return False

        return True

    # 1. node is indexed uniquly with the number from 0 to n - 1;
    # 2. DFS go traverse the graph, while color node alternatively changed with 0/1
    def isBipartite158msSolutionWithRecursion(self, graph: List[List[int]]) -> bool:
        colored = {}  # dictionary to record the node is colored or not.

        def dfs(cur_node):
            for nxt in graph[cur_node]:
                if nxt in colored:
                    if colored[nxt] == colored[cur_node]:  # means two connected node with the same color
                        return False
                else:  # otherwise, set it to a different color of its neighbour
                    colored[nxt] = 1 - colored[
                        cur_node]  # if this node is not colored before, we color it with alternative color
                    if not dfs(nxt):  # and further dfs it next node
                        return False
            return True

        for i in range(len(graph)):
            if i not in colored:
                colored[i] = 0
                if not dfs(i):
                    return False

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isBipartite([
        [], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9],
        [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]
    ]))
