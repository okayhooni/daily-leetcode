"""
https://leetcode.com/problems/evaluate-division/
"""
from typing import List, Dict, Tuple, Set, Optional
from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def _recursive_path_search(a_node: str, b_node: str, visited: Optional[Set[str]] = None):
            if (a_node, b_node) in cache:
                return cache[a_node, b_node]

            if visited is None:
                visited = set()

            visited.add(a_node)

            for neighbor_node, cur_val in graph[a_node]:
                if neighbor_node in visited:
                    continue
                # print(visited)
                recursive_checked_val = _recursive_path_search(neighbor_node, b_node, visited=visited)
                # print(a_node, neighbor_node, recursive_checked_val)
                if recursive_checked_val != -1.:
                    cumul_val = cur_val * recursive_checked_val
                    # print('cumul_val:', cumul_val)
                    cache[a_node, b_node] = cumul_val
                    cache[b_node, a_node] = 1 / cumul_val
                    return cumul_val

            cache[a_node, b_node] = -1.
            cache[b_node, a_node] = -1.
            return -1.

        existing_members = set(member for pair in equations for member in pair)

        graph: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
        cache: Dict[Tuple[str, str], float] = {
            (member, member): 1. for member in existing_members
        }

        for (a, b), val in zip(equations, values):
            # a / b = val
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))
            cache[a, b] = val
            cache[b, a] = 1 / val

        # print(graph)
        output = [
            _recursive_path_search(a, b)
            for a, b in queries
        ]
        # print(cache)
        return output

    def calcEquation17msSolWithQueueBFS(
            self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = {}

        def build_graph(equations, values):
            def add_edge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]

            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1 / value)

        def find_path(query):
            b, e = query

            if b not in graph or e not in graph:
                return -1.0

            q = deque([(b, 1.0)])
            visited = set()

            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product * value))

            return -1.0

        build_graph(equations, values)
        return [find_path(q) for q in queries]


if __name__ == '__main__':
    sol = Solution()
    print(sol.calcEquation(
        [["a", "b"], ["b", "c"]],
        [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    ))
