"""
https://leetcode.com/problems/top-k-frequent-elements/
"""
import heapq
from typing import List
from collections import Counter


class Solution:
    """
    모든 풀이 공통

    m: the number of unique elements in the array

    시간 복잡도: O(n) + O(m*log(n))
    공간 복잡도: O(m)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        heap = []

        for n, cnt in nums_counter.items():
            heapq.heappush(heap, (-cnt, n))

        return [
            heapq.heappop(heap)[1]
            for _ in range(k)
        ]

    # Given an integer array nums and an integer k, return the k most frequent elements.
    # You may return the answer in "any order".
    def topKFrequentMinHeap(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        heap = []

        for n, cnt in nums_counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, n))
            elif heap[0][0] < cnt:
                heapq.heapreplace(heap, (cnt, n))
                # This one step operation is more efficient than a heappop() followed by heappush()
                # and can be more appropriate when using a fixed-size heap.

        # slightly more efficient! (there is no heappop operation)
        return [tup[1] for tup in heap]

    def topKFrequent_OneLine(self, nums: List[int], k: int) -> List[int]:
        return [n for n, _ in Counter(nums).most_common(k)]

    def topKFrequent_OneLine2(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]
