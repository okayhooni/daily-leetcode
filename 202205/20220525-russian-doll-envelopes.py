"""
https://leetcode.com/problems/russian-doll-envelopes/

> Topic: Dynamic Programming / Binary Search / Sorting

Ref) https://dev.to/seanpgallivan/solution-russian-doll-envelopes-459i
"""
from typing import List
from bisect import bisect_left
# print(str.lower('A'))


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        dp = []
        for _, height in envelopes:
            left = bisect_left(dp, height)
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height
        print(dp)
        return len(dp)

    def maxEnvelopesBruteDP(self, envelopes: List[List[int]]) -> int:
        """
        Time Limit Exceeded
        """
        envelopes.sort()
        print(envelopes)
        dp = [1 for _ in range(len(envelopes))]
        for idx, (width, height) in enumerate(envelopes):
            if idx == 0:
                continue

            # for prev_dp_val, (prev_width, prev_height) in zip(dp[idx - 1::-1], envelopes[idx - 1::-1]):
            #     if prev_width < width and prev_height < height:
            #         dp[idx] += prev_dp_val
            #         break
            try:
                dp[idx] += max(
                    prev_dp_val
                    for prev_dp_val, (prev_width, prev_height) in zip(dp[idx - 1::-1], envelopes[idx - 1::-1])
                    if prev_width < width and prev_height < height
                )
            except ValueError:
                pass

        print(dp)
        return max(dp)


if __name__ == '__main__':
    test_case = [[5, 4], [5, 5], [6, 4], [6, 7], [2, 3], [5, 1]]
    sol = Solution()
    print(sol.maxEnvelopes(test_case))
    print(sol.maxEnvelopesBruteDP(test_case))
    print(sol.maxEnvelopesBruteDP([[10, 8], [1, 12], [6, 15], [2, 18]]))
    print(sol.maxEnvelopesBruteDP([[46, 89], [50, 53], [52, 68], [72, 45], [77, 81]]))
