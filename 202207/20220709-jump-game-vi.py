"""
https://leetcode.com/problems/jump-game-vi/

> Topic: Dynamic Programming / Queue / Heap (Priority Queue) / Sliding Window

Hint)
- Let dp[i] be "the maximum score to reach the end starting at index i".
  The answer for dp[i] is nums[i] + max{dp[i+j]} for 1 <= j <= k. That gives an O(n*k) solution.
- Instead of checking every j for every i,
  keep track of the largest dp[i] values in a heap and calculate dp[i] from right to left.
  When the largest value in the heap is out of bounds of the current index, remove it and keep checking.

Ref) https://dev.to/seanpgallivan/solution-jump-game-vi-4a2
"""
from typing import *
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deq = deque([n-1])
        for i in range(n-2, -1, -1):
            if deq[0] - i > k: deq.popleft()
            nums[i] += nums[deq[0]]
            while len(deq) and nums[deq[-1]] <= nums[i]: deq.pop()
            deq.append(i)
        return nums[0]
