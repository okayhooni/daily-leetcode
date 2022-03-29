"""
https://leetcode.com/problems/find-the-duplicate-number/

관련 이론) Floyd's cycle detection (Floyd's Tortoise & Hare Algorithm) -> 러너 풀이(토끼와 거북이)
- https://www.youtube.com/watch?v=LUm2ABqAs1w
- https://www.youtube.com/watch?v=gBTe7lFR3vc

참고)
- https://velog.io/@wannte/Find-the-Duplicate-NumberLeet-Code
- https://velog.io/@hojin11choi/TIL-LeetCode-141-feat.-Floyds-Cycle-Detection-Algorithm
- https://stackoverflow.com/questions/47193225/runtime-complexity-of-floyds-cycle-detection

관련 문제)
- https://leetcode.com/problems/linked-list-cycle/
- https://leetcode.com/problems/linked-list-cycle-ii/
"""
from typing import List
from collections import Counter


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(n)
        """
        return Counter(nums).most_common(1)[0][0]

    # Follow up:
    # How can we prove that at least one duplicate number must exist in nums? -> If it has CYCLE, it has DUPLICATE nums.
    # Can you solve the problem in linear runtime complexity? -> Floyd's Tortoise & Hare Algorithm
    # (You must solve the problem without modifying the array nums and uses only constant extra space.)
    def findDuplicate_solution(self, nums):
        """
        시간 복잡도: O(n)
        공간 복잡도: O(1)
        """
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
