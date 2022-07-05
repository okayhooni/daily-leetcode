"""
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

> Topic: Union-Find / Hash Table (Set/Dict)

cf)
- https://leetcode.com/problems/smallest-string-with-swaps/
- https://leetcode.com/problems/critical-connections-in-a-network/

Ref)
- https://dev.to/theabbie/longest-consecutive-sequence-19e7
- https://dev.to/seanpgallivan/solution-longest-consecutive-sequence-27ni
- https://github.com/azl397985856/leetcode/blob/master/problems/128.longest-consecutive-sequence.md

union-find approach and/or dynamic programming (DP) approach;
"""
from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len_ans = 0
        for num in nums:
            if (num - 1) not in nums_set:  # start num of the streak
                cur_len = 1
                while (num + cur_len) in nums_set:
                    cur_len += 1
                max_len_ans = max(max_len_ans, cur_len)
        return max_len_ans

    def longestConsecutive2(self, nums: List[int]) -> int:
        nmap, seen, ans = {}, [0] * len(nums), 0
        for i, n in enumerate(nums):
            nmap[n] = i
            # if n not in nmap:
            #     nmap[n] = i

        for n in nums:
            if seen[nmap[n]]:
                continue

            curr, count = n, 1
            while curr + 1 in nmap:
                curr += 1
                ix = nmap[curr]
                if seen[ix]:
                    count += seen[ix]
                    break
                else:
                    seen[ix] = 1
                    count += 1
            seen[nmap[n]], ans = count, max(ans, count)
        return ans

    def longestConsecutiveTimeLimitExceeded(self, nums: List[int]) -> int:
        """
        Time Limit Exceeded
        """
        if not nums:
            return 0

        min_num, max_num = min(nums), max(nums)
        board = [False for _ in range(max_num - min_num + 1)]

        for n in nums:
            board[n - min_num] = True

        longest_ans = cur_len = cur_num_cnt = 0
        for has_num in board:
            if has_num:
                cur_len += 1
                cur_num_cnt += 1
                if cur_num_cnt == len(nums):
                    break
            elif cur_len:
                longest_ans = max(longest_ans, cur_len)
                cur_len = 0

        return max(longest_ans, cur_len)


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestConsecutive2([100, 4, 200, 1, 3, 2]) == 4
    assert sol.longestConsecutive2([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert sol.longestConsecutive2([0, 1, 2, 4, 8, 5, 6, 7, 9, 3, 55, 88, 77, 99, 999999999]) == 10
