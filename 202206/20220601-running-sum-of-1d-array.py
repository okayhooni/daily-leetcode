"""
https://leetcode.com/problems/running-sum-of-1d-array/

Hint) Think about how we can calculate the i-th number in the running sum from the (i-1)-th number.
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            try:
                prev = res[-1]
            except IndexError:
                prev = 0

            res.append(prev + n)

        return res
