"""
https://leetcode.com/problems/permutations-ii/
"""
from typing import List, Set, Tuple, Counter as CounterType
from itertools import permutations
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        input_nums_len = len(nums)

        def dfs(remain_multiset: CounterType[int], path: List[int]):
            if len(path) == input_nums_len:
                res.append(path)
                return

            for key_num in list(remain_multiset.keys()):
                remain_multiset[key_num] -= 1
                if remain_multiset[key_num] == 0:
                    del remain_multiset[key_num]

                dfs(remain_multiset, path + [key_num])

                remain_multiset[key_num] += 1

        dfs(Counter(nums), [])
        return res

    def permuteUniqueUsingBuiltIn(self, nums: List[int]) -> List[List[int]]:
        permutation_with_duplicates = permutations(nums)
        return list(set(permutation_with_duplicates))

    def permuteUniqueBruteForceDFS(self, nums: List[int]) -> List[List[int]]:
        all_unique_sets: Set[Tuple[int, ...]] = set()

        def dfs(remain_elements: List[int], cur_elements: List[int]):
            if len(remain_elements) == 0:
                all_unique_sets.add(tuple(cur_elements))

            for e in remain_elements:
                next_elements = remain_elements[:]
                next_elements.remove(e)

                dfs(next_elements, cur_elements + [e])

        dfs(nums, [])
        return list(all_unique_sets)


if __name__ == '__main__':
    test_case = [1, 1, 2]
    sol = Solution()
    print(sol.permuteUnique(test_case))
    print(sol.permuteUniqueUsingBuiltIn(test_case))
    print(sol.permuteUniqueBruteForceDFS(test_case))
