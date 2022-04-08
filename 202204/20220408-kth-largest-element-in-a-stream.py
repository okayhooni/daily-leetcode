"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
import heapq
from typing import List
from bisect import insort


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        시간 복잡도: O(n * log(n))
        공간 복잡도: O(n)
        """
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        """
        시간 복잡도: O(log(n)) ~ 최악 O(n)
        """
        insort(self.nums, val)
        return self.nums[len(self.nums) - self.k]


class KthLargestWithHeap80msSolution:
    def __init__(self, k, nums):
        """
        시간 복잡도: O(n)
        공간 복잡도: O(n) -> O(k)
        """
        self.nums = nums
        self.k = k
        # build min heap
        heapq.heapify(self.nums)
        # remove n - k smallest number
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        """
        시간 복잡도: O(log(k))
        """
        # add to heaq if it's less then k
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            # if len(heaq) == k, and val greater than smallest num
            # then pop smallest num than add val to heap
            heapq.heapreplace(self.nums, val)
            # = heapq.heappushpop(self.heap, val)
        # return k largest
        return self.nums[0]
