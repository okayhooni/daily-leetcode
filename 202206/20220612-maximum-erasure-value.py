"""
https://leetcode.com/problems/maximum-erasure-value/

> Topic: Two Pointers (Double Pointer) / Sliding Window / Hash Table (Set/Dict)

cf)
- https://leetcode.com/problems/longest-substring-without-repeating-characters/
- https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
- https://leetcode.com/problems/132-pattern/

Hint 1) The main point here is for the subarray to contain unique elements for each index.
Only the first subarrays starting from that index have unique elements.

Hint 2) This can be solved using the two pointers technique

Ref)
- https://dev.to/seanpgallivan/solution-maximum-erasure-value-1kod
"""
from typing import List
from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N) where N is the length of nums
        """
        seen_num_to_idx_map = {}
        cur_start_idx = 0
        max_unique_sum = cur_unique_sum = 0

        for cur_idx, cur_num in enumerate(nums):
            prev_idx_of_cur_num = seen_num_to_idx_map.get(cur_num)
            if prev_idx_of_cur_num is not None and cur_start_idx <= prev_idx_of_cur_num:
                prev_start_idx, cur_start_idx = cur_start_idx, prev_idx_of_cur_num + 1
                cur_unique_sum -= sum(nums[prev_start_idx:cur_start_idx - 1])
            else:
                cur_unique_sum += cur_num
                max_unique_sum = max(max_unique_sum, cur_unique_sum)

            seen_num_to_idx_map[cur_num] = cur_idx

        return max_unique_sum

    def maximumUniqueSubarray2(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N) where N is the length of nums - all the numbers on the input can be popped at most once!
        """
        total, best, left_idx = 0, 0, 0
        cnt_by_num_map = defaultdict(int)
        for cur_right_num in nums:
            cnt_by_num_map[cur_right_num] += 1
            total += cur_right_num
            if cnt_by_num_map[cur_right_num] > 1:
                while cnt_by_num_map[cur_right_num] > 1:  # eager
                    cnt_by_num_map[nums[left_idx]] -= 1
                    total -= nums[left_idx]
                    left_idx += 1
            else:
                best = max(best, total)
        return best
