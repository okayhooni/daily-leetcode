"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

> Topic: Prefix Sum (cumulative sum, inclusive scan) / Two Pointer & Sliding Window

cf) https://leetcode.com/problems/range-sum-query-2d-immutable/

ref) https://dev.to/seanpgallivan/solution-maximum-points-you-can-obtain-from-cards-2no

Since we're forced to take K amount of cards no matter what,
we can solve this problem with a two-pointer system with a sliding window approach.
Instead of counting the sum of the values between the two pointers,
we'll instead be counting the sum of the values outside the sliding window.
"""
from typing import *


class Solution:
    def maxScore(self, card_points: List[int], k: int) -> int:
        """
        Time Complexity: O(K)
        Space Complexity: O(1)
        """
        if len(card_points) == k:
            return sum(card_points)

        left_score = 0
        right_score = sum(card_points[-k-1:])
        max_score = -1
        for left in range(k + 1):
            if 0 < left:
                left_score += card_points[left-1]

            right = k - left
            if right >= 0:
                right_score -= card_points[len(card_points)-right-1]

            # print(left_score, right_score)
            max_score = max(max_score, left_score + right_score)

        return max_score

    def maxScoreBrute(self, card_points: List[int], k: int) -> int:
        """
        Time Complexity: O(K)
        Space Complexity: O(N)
        """
        left_to_right_prefix_sum, right_to_left_prefix_sum = card_points[:], card_points[:]
        for idx in range(1, len(card_points)):
            left_to_right_prefix_sum[idx] += left_to_right_prefix_sum[idx - 1]
        for idx in reversed(range(len(card_points) - 1)):
            right_to_left_prefix_sum[idx] += right_to_left_prefix_sum[idx + 1]

        # print(left_to_right_prefix_sum)
        # print(right_to_left_prefix_sum)

        max_score = -1
        for left in range(k + 1):
            if left == 0:
                left_score = 0
            else:
                left_score = left_to_right_prefix_sum[left-1]

            right = k - left
            if right == 0:
                right_score = 0
            else:
                right_score = right_to_left_prefix_sum[len(card_points)-right]

            max_score = max(max_score, left_score + right_score)

        return max_score

    def maxScoreRef(self, card_points: List[int], k: int) -> int:
        """
        Time Complexity: O(K)
        Space Complexity: O(1)
        """
        best = total = sum(card_points[:k])
        for i in range(k - 1, -1, -1):
            total += card_points[i + len(card_points) - k] - card_points[i]
            best = max(best, total)
        return best


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12
    assert sol.maxScore([2, 2, 2], 2) == 4
    assert sol.maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55
    assert sol.maxScoreRef([1, 2, 3, 4, 5, 6, 1], 3) == 12
    assert sol.maxScoreRef([9, 7, 7, 9, 7, 7, 9], 7) == 55
