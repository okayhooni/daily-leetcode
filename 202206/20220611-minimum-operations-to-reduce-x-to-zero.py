"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

> Topic: Two Pointers (Double Pointer) / Sliding Window

Hint 1) Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.
Hint 2) Finding the maximum subarray is standard and can be done greedily.

Ref)
- https://dev.to/ruarfff/day-14-minimum-operations-to-reduce-x-to-zero-47dp
- https://velog.io/@jiselectric/Leetcode-Minimum-Operations-to-Reduce-X-to-Zero
- https://github.com/azl397985856/leetcode/blob/master/problems/1658.minimum-operations-to-reduce-x-to-zero.md
[Reversed Sliding Window]
- https://www.geeksforgeeks.org/minimum-number-of-array-elements-from-either-ends-required-to-be-subtracted-from-x-to-reduce-x-to-0/

Using sliding window algorithm,
simply set the range of elements within the array with maximum sum which equals the target
(sum of entire array minus the input x).
And then after storing the maximum length of two indices left and right,
subtract the value to the total length of array
"""
from typing import List, Union
from functools import cache


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Time Complexity: O(N)
        (Extra) Space Complexity: O(1)
        """
        i = 0
        target = sum(nums) - x
        win = 0
        ans = len(nums)

        if target == 0:
            return ans

        for j in range(len(nums)):
            win += nums[j]
            while i < j and win > target:
                win -= nums[i]
                i += 1
            if win == target:
                ans = min(ans, len(nums) - (j - i + 1))
        return -1 if ans == len(nums) else ans

    def minOperationsRef(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x

        if target == 0:
            return len(nums)

        left, right = 0, 0
        curr, cnt = 0, 0

        while right < len(nums):
            curr = curr + nums[right]

            while left < right and curr > target:
                curr = curr - nums[left]
                left = left + 1
            if curr == target:
                cnt = max(cnt, right - left + 1)
            right = right + 1

        if cnt == 0:
            return -1
        else:
            return len(nums) - cnt

def minOperationsWithNaiveBacktracking(self, nums: List[int], x: int) -> int:
        """
        Time Limit Exceeded -(with DP)-> Memory Limit Exceeded
        """
        @cache
        def backtrack(left: int, right: int, remaining_x: int) -> Union[int, float]:
            if left > right:
                return float('inf')

            if nums[left] == remaining_x or nums[right] == remaining_x:
                return 1

            if nums[left] < x:
                left_ans = backtrack(left + 1, right, remaining_x - nums[left])
            else:
                left_ans = float('inf')

            if nums[right] < x:
                right_ans = backtrack(left, right - 1, remaining_x - nums[right])
            else:
                right_ans = float('inf')

            return 1 + min(left_ans, right_ans)

        ans = backtrack(left=0, right=len(nums) - 1, remaining_x=x)
        return -1 if ans == float('inf') else ans


if __name__ == '__main__':
    sol = Solution()
    # print(sol.minOperations([1, 1, 4, 2, 3], 5))
    test_arr = [1241,8769,9151,3211,2314,8007,3713,5835,2176,8227,5251,9229,904,1899,5513,7878,8663,3804,2685,3501,1204,9742,2578,8849,1120,4687,5902,9929,6769,8171,5150,1343,9619,3973,3273,6427,47,8701,2741,7402,1412,2223,8152,805,6726,9128,2794,7137,6725,4279,7200,5582,9583,7443,6573,7221,1423,4859,2608,3772,7437,2581,975,3893,9172,3,3113,2978,9300,6029,4958,229,4630,653,1421,5512,5392,7287,8643,4495,2640,8047,7268,3878,6010,8070,7560,8931,76,6502,5952,4871,5986,4935,3015,8263,7497,8153,384,1136]
    test_x = 894887480
    print(sol.minOperations(test_arr, test_x))
    # print(sol.minOperationsWithNaiveBacktracking(test_arr, test_x))
