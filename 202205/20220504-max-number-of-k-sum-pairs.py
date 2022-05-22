"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/

cf) https://leetcode.com/problems/container-with-most-water/
cf) https://leetcode.com/problems/3sum/
"""
from typing import List
from collections import deque, Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        시간 복잡도: O(n * log(n))
        공간 복잡도: O(1) ~ in-place sort
        """
        nums.sort()
        res_cnt = 0
        left_idx, right_idx = 0, len(nums) - 1

        while left_idx < right_idx:
            cur_pair_sum = nums[left_idx] + nums[right_idx]

            if cur_pair_sum > k:
                right_idx -= 1
            elif cur_pair_sum < k:
                left_idx += 1
            else:
                right_idx -= 1
                left_idx += 1
                res_cnt += 1

        return res_cnt

    def maxOperationsWithDeque(self, nums: List[int], k: int) -> int:
        """
        시간 복잡도: O(n * log(n))
        공간 복잡도: O(n)
        """
        dq = deque(sorted(nums))
        res_cnt = 0

        while len(dq) >= 2:
            cur_pair_sum = dq[0] + dq[-1]

            if cur_pair_sum > k:
                dq.pop()
            elif cur_pair_sum < k:
                dq.popleft()
            else:
                dq.pop()
                dq.popleft()
                res_cnt += 1

        return res_cnt

    def maxOperations640msSol(self, nums: List[int], k: int) -> int:
        """
        The number of such pairs equals to min(count(x), count(k-x)),
        unless that x = k / 2, where the number of such pairs will be floor(count(x) / 2).

        시간 복잡도: O(n)
        공간 복잡도: O(n)
        """
        counter = Counter(nums)
        res = 0

        while counter:
            n, c = counter.popitem()
            complement = k - n
            if complement == n:
                res += c // 2
            elif complement in counter:
                res += min(c, counter[complement])
                counter.pop(complement)

        return res
