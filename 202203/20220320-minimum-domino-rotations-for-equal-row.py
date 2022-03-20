"""
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
"""
from typing import List

INF = float('inf')


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        brute force 풀이

        시간 복잡도: O(n)
        공간 복잡도: O(n)
        """
        dice_cnt = len(tops)
        top_by_num = [[0 for _ in range(dice_cnt)] for _ in range(6)]
        bottom_by_num = [[0 for _ in range(dice_cnt)] for _ in range(6)]
        result_rotate_cnt = INF

        for ith_domino, (top_num, bottom_num) in enumerate(zip(tops, bottoms)):
            top_by_num[top_num - 1][ith_domino] = 1
            bottom_by_num[bottom_num - 1][ith_domino] = 1

        for domino_num, (specific_nums_on_top, specific_nums_on_bottom) in enumerate(zip(top_by_num, bottom_by_num), 1):
            censor_on_cur_candidate_num = [top + bottom for top, bottom in
                                           zip(specific_nums_on_top, specific_nums_on_bottom)]

            if not all(censor_on_cur_candidate_num):
                continue

            num_cnt_on_top_side, num_cnt_on_bottom_side = sum(specific_nums_on_top), sum(specific_nums_on_bottom)
            most_num_cnt_on_side = max(num_cnt_on_top_side, num_cnt_on_bottom_side)

            result_rotate_cnt = min(result_rotate_cnt, dice_cnt - most_num_cnt_on_side)

        return -1 if result_rotate_cnt == INF else result_rotate_cnt

    def minDominoRotations_1064ms_sample(self, tops: List[int], bottoms: List[int]) -> int:
        """
        greedy 한 수학적 풀이

        시간 복잡도: O(n)
        공간 복잡도: O(1)
        """
        for x in [tops[0], bottoms[0]]:  # 첫번쨰 도미노에 있는 수 2개로만 가지치기
            if all(x in d for d in zip(tops, bottoms)):
                return len(tops) - max(tops.count(x), bottoms.count(x))  # 바로 리턴(수학적으로 이면체에 대해선 당연함)
        return -1
