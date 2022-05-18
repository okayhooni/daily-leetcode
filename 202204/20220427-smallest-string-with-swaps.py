"""
https://leetcode.com/problems/smallest-string-with-swaps/

- Think of it as a graph problem.
- Consider the pairs as connected nodes in the graph, what can you do with a connected component of indices ?
- We can sort each connected component alone to get the lexicographically minimum string.

> Topic: Union-Find
"""
from typing import List, Dict, Set
import heapq
from collections import defaultdict


class Solution:
    class UnionFind:
        def __init__(self, n: int):
            self.cluster_root_id = list(range(n))

        def union(self, a_idx: int, b_idx: int) -> None:
            self.cluster_root_id[self.find(b_idx)] = self.find(a_idx)

        def find(self, idx: int) -> int:
            if self.cluster_root_id[idx] != idx:
                # return self.find(self.cluster_root_id[idx])
                self.cluster_root_id[idx] = self.find(self.cluster_root_id[idx])

            return self.cluster_root_id[idx]

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        REF:
        - https://withhamit.tistory.com/270
        - https://walkccc.me/LeetCode/problems/1202/
        - https://null00.medium.com/leetcode-smallest-string-with-swaps-b5ae88b01b47

        시간 복잡도: O(n * log(n))
        공간 복잡도: O(n)
        """
        uf = self.UnionFind(len(s))
        heap_clusters_by_root_idx = defaultdict(list)
        # print(uf.cluster_root_id)
        # print('==========')

        for a_idx, b_idx in pairs:
            uf.union(a_idx, b_idx)
            # print(uf.cluster_root_id)

        # print('==========')

        for i in range(len(s)):
            heapq.heappush(heap_clusters_by_root_idx[uf.find(i)], s[i])
            # print(uf.cluster_root_id)

        # print(heap_clusters_by_root_idx)

        smallest_list = [
            heapq.heappop(heap_clusters_by_root_idx[uf.find(i)])
            for i in range(len(s))
        ]

        return ''.join(smallest_list)

    def smallestStringWithSwapsWithDFS(self, s: str, pairs: List[List[int]]) -> str:
        """
        REF: https://yjam.tistory.com/25

        시간 복잡도: O(n * log(n))
        공간 복잡도: O(n)
        """

        def dfs(idx: int, cluster_idx_list: List[int]):
            visited_idx.add(idx)
            cluster_idx_list.append(idx)

            for j in graph[idx]:
                if j not in visited_idx:
                    dfs(j, cluster_idx_list)

        # graph = [[] for _ in range(len(s))]
        # for i, j in pairs:
        #     graph[i].append(j)
        #     graph[j].append(i)
        graph = defaultdict(list)
        for a_idx, b_idx in pairs:
            graph[a_idx].append(b_idx)
            graph[b_idx].append(a_idx)

        smallest_list = list(s)
        visited_idx = set()

        for i in range(len(s)):
            if i not in visited_idx:
                cur_cluster_idx_list = []
                dfs(i, cur_cluster_idx_list)
                # print(cur_cluster_idx_list)
                cur_cluster_idx_list.sort()
                cur_sorted_chars = sorted(s[idx] for idx in cur_cluster_idx_list)
                print(cur_sorted_chars)

                for idx, char in zip(cur_cluster_idx_list, cur_sorted_chars):
                    smallest_list[idx] = char

        return ''.join(smallest_list)

    def smallestStringWithSwapsWithClusters(self, s: str, pairs: List[List[int]]) -> str:
        """
        Time Limit Exceeded
        """
        map_idx_to_cluster_id = {}
        clusters: Dict[int, Set] = defaultdict(set)
        last_cluster_id = 0

        for a_idx, b_idx in pairs:
            a_cluster_id = map_idx_to_cluster_id.get(a_idx)
            b_cluster_id = map_idx_to_cluster_id.get(b_idx)

            if a_cluster_id is None and b_cluster_id is None:
                last_cluster_id += 1
                clusters[last_cluster_id].update({a_idx, b_idx})
                map_idx_to_cluster_id[a_idx] = last_cluster_id
                map_idx_to_cluster_id[b_idx] = last_cluster_id
            elif a_cluster_id is None:
                clusters[b_cluster_id].add(a_idx)
                map_idx_to_cluster_id[a_idx] = b_cluster_id
            elif b_cluster_id is None:
                clusters[a_cluster_id].add(b_idx)
                map_idx_to_cluster_id[b_idx] = a_cluster_id
            else:
                merged_cluster_id, removed_cluster_id = sorted([a_cluster_id, b_cluster_id])
                migrated = clusters.pop(removed_cluster_id)
                clusters[merged_cluster_id] |= migrated
                for idx in migrated:
                    map_idx_to_cluster_id[idx] = merged_cluster_id

        # print(clusters)
        smallest_list = list(s)

        for idx_set in clusters.values():
            sorted_idx = sorted(idx_set)
            connected_chars = [s[idx] for idx in sorted_idx]
            connected_chars.sort()

            for idx, char in zip(sorted_idx, connected_chars):
                smallest_list[idx] = char

        return ''.join(smallest_list)

    def smallestStringWithSwapsWithGreedyApproach(self, s: str, pairs: List[List[int]]) -> str:
        """
        Wrong answer, because it's not greedy
        """
        heap = [s]
        discovered = {s}
        smallest_str = None

        while heap:
            cur_smallest_str = heapq.heappop(heap)
            print('cur_smallest_str:', cur_smallest_str, '/ smallest_str:', smallest_str)
            if smallest_str is not None and smallest_str <= cur_smallest_str:
                break

            smallest_str = cur_smallest_str

            for a_idx, b_idx in pairs:
                cur_candidate_str = smallest_str[:a_idx] + smallest_str[b_idx] \
                    + smallest_str[a_idx + 1:b_idx] + smallest_str[a_idx] \
                    + smallest_str[b_idx+1:]

                if cur_candidate_str not in discovered:
                    discovered.add(cur_candidate_str)
                    heapq.heappush(heap, cur_candidate_str)

            print(heap)

        return smallest_str


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]]))
    print(sol.smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]]))
    print(sol.smallestStringWithSwapsWithDFS("dcab", [[0, 3], [1, 2]]))
    print(sol.smallestStringWithSwapsWithDFS("dcab", [[0, 3], [1, 2], [0, 2]]))
