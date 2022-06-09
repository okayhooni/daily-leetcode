"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

> Topic: Two Pointers (Double Pointer)

cf)
- https://leetcode.com/problems/max-number-of-k-sum-pairs/
- https://leetcode.com/problems/container-with-most-water/
- https://leetcode.com/problems/3sum/
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            cur_sum = numbers[start] + numbers[end]
            if cur_sum == target:
                break
            elif cur_sum < target:
                start += 1
            else:
                end -= 1

        return [start + 1, end + 1]
