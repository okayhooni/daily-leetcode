"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

> Topic: Heap (Priority Queue) / Quick Select

Ref)
- https://dev.to/theabbie/kth-largest-element-in-an-array-ike
- https://github.com/azl397985856/leetcode/blob/master/problems/215.kth-largest-element-in-an-array.md
"""
from typing import List
from heapq import heappush, heappop, heapify, heapreplace, heappushpop  # , nlargest


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapify(heap)

        for _ in range(k - 1):
            heappop(heap)

        return -heappop(heap)

    def findKthLargestRef(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]

    def findKthLargestFinal(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)
        for idx in range(k, len(nums)):
            heappushpop(heap, nums[idx])

        return heap[0]


def nlargest(n, iterable, key=None):
    """Find the n largest elements in a dataset.

    Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]
    """

    # Short-cut for n==1 is to use max()
    if n == 1:
        it = iter(iterable)
        sentinel = object()
        result = max(it, default=sentinel, key=key)
        return [] if result is sentinel else [result]

    # When n>=size, it's faster to use sorted()
    try:
        size = len(iterable)
    except (TypeError, AttributeError):
        pass
    else:
        if n >= size:
            return sorted(iterable, key=key, reverse=True)[:n]

    # When key is none, use simpler decoration
    if key is None:
        it = iter(iterable)
        result = [(elem, i) for i, elem in zip(range(0, -n, -1), it)]
        if not result:
            return result
        heapify(result)
        top = result[0][0]
        order = -n
        _heapreplace = heapreplace
        for elem in it:
            if top < elem:
                _heapreplace(result, (elem, order))
                top, _order = result[0]
                order -= 1
        result.sort(reverse=True)
        return [elem for (elem, order) in result]

    # General case, slowest method
    it = iter(iterable)
    result = [(key(elem), i, elem) for i, elem in zip(range(0, -n, -1), it)]
    if not result:
        return result
    heapify(result)
    top = result[0][0]
    order = -n
    _heapreplace = heapreplace
    for elem in it:
        k = key(elem)
        if top < k:
            _heapreplace(result, (k, order, elem))
            top, _order, _elem = result[0]
            order -= 1
    result.sort(reverse=True)
    return [elem for (k, order, elem) in result]
