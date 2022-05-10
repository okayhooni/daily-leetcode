"""
https://leetcode.com/problems/combination-sum-iii/
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        # remains_sum = sum(candidates)

        def dfs(
            target_sum: int,
            remains_sum: int,
            remain_candidate_start_idx: int,
            remain_count: int,
            cur_combination_path: List[int]
        ):
            # nonlocal remains_sum

            if remain_count < 0:
                return

            if target_sum > remains_sum:
                return
            elif target_sum < 0:
                return
            elif target_sum == 0 and remain_count == 0:
                results.append(cur_combination_path)

            for cur_candidate_idx in range(remain_candidate_start_idx, len(candidates)):
                cur_candidate_num = candidates[cur_candidate_idx]
                # remains_sum -= cur_candidate_num

                dfs(
                    target_sum=target_sum - cur_candidate_num,
                    remains_sum=remains_sum - cur_candidate_num,
                    remain_candidate_start_idx=cur_candidate_idx + 1,
                    remain_count=remain_count - 1,
                    cur_combination_path=cur_combination_path + [cur_candidate_num],
                )

                # remains_sum += cur_candidate_num

        results = []
        dfs(
            target_sum=n,
            remains_sum=sum(candidates),
            remain_candidate_start_idx=0,
            remain_count=k,
            cur_combination_path=[],
        )
        return results
