"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""
from typing import List
import heapq


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(n * log(n))
    공간 복잡도: O(n)
    """
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sorted_list = sorted(enumerate(mat), key=lambda r: sum(r[1]))
        return [row[0] for row in sorted_list[:k]]

    def kWeakestRows_96ms_sample(self, mat: List[List[int]], k: int) -> List[int]:
        """
        heappush 에 시간복잡도 O(log(n)) 소요되므로, 다른 풀이에 비해 시간복잡도 상의 이득은 미미
        """
        heap = []
        heapq.heapify(heap)
        for row in range(len(mat)):
            heapq.heappush(heap, mat[row].count(1) + row / 100)
        result = []
        for _ in range(k):
            el = heapq.heappop(heap)
            result.append(round((el - int(el)) * 100))
        return result

    def kWeakestRows_100ms_sample(self, mat: List[List[int]], k: int) -> List[int]:
        ans = {}
        for i in range(len(mat)):
            ans[i] = sum(mat[i])
        ans = sorted(ans, key=ans.get)
        return ans[:k]
