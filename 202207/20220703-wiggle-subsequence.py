"""
https://leetcode.com/problems/wiggle-subsequence/

> Topic: Math / Greedy Algorithm / Dynamic Programming

> Follow up: Could you solve this in O(n) time?

Ref) https://dev.to/seanpgallivan/solution-wiggle-subsequence-3e65

any number that lies in the middle of a stretch of the same direction is extraneous,
because the more extreme numbers are the better choices to keep,
as they allow for a larger likelihood that a subsequent number will be a directional change.
"""
from typing import *


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans_max_len = 0
        is_up = None
        prev_num = None

        for n in nums:
            if prev_num is None:
                prev_num = n
                ans_max_len += 1
                continue

            cur_delta = n - prev_num

            if cur_delta > 0:
                if is_up is False or is_up is None:
                    ans_max_len += 1
                is_up = True
            elif cur_delta < 0:
                if is_up is True or is_up is None:
                    ans_max_len += 1
                is_up = False

            prev_num = n

        return ans_max_len


if __name__ == "__main__":
    sol = Solution()
    assert sol.wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6
    assert sol.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
    assert sol.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
