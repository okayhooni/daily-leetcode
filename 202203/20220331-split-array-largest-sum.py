"""
https://leetcode.com/problems/split-array-largest-sum/
"""
from typing import List

INF = float('inf')


class Solution:
    def splitArrayWithDp(self, nums: List[int], m: int) -> int:
        """
        Time Limit Exceeded

        시간 복잡도: O(n^2 * m)
        공간 복잡도: O(n)
        """
        if m == 1:
            return sum(nums)

        dp_tabulation = [[
            INF for _ in range(len(nums) + 1)
        ] for _ in range(2)]
        dp_tabulation[0][0] = 0
        dp_tabulation[1][0] = 0

        cumulative_sum = [0]
        for num in nums:
            cumulative_sum.append(cumulative_sum[-1] + num)

        for m_split_num in range(1, m + 1):
            for sub_prob_len in range(1, len(nums) + 1):
                for sub_chunk_end_idx in range(m_split_num - 1, sub_prob_len):

                    dp_tabulation[m_split_num % 2][sub_prob_len] = min(
                        dp_tabulation[m_split_num % 2][sub_prob_len],
                        max(
                            dp_tabulation[(m_split_num - 1) % 2][sub_chunk_end_idx],
                            cumulative_sum[sub_prob_len] - cumulative_sum[sub_chunk_end_idx],
                        )
                    )

        return int(dp_tabulation[m % 2][-1])

    def splitArrayWithBinarySearch(self, nums: List[int], m: int) -> int:
        """
        시간 복잡도: O(n * log(n))
        공간 복잡도: O(1)
        """
        def _can_be_split(target: int) -> bool:
            cur_sum, arr_cnt = 0, 1  # 0
            for n in nums:
                cur_sum += n
                if cur_sum > target:
                    arr_cnt += 1
                    if arr_cnt > m:
                        return False
                    cur_sum = n

            return True

        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2

            if _can_be_split(mid):
                right = mid  # - 1
            else:
                left = mid + 1

        return right
