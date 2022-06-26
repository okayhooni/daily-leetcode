"""
https://leetcode.com/problems/range-sum-query-2d-immutable/

> Topic: Prefix Sum (cumulative sum, inclusive scan)

cf) https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

ref)
- https://dev.to/seanpgallivan/solution-range-sum-query-2d-immutable-9ic
- https://dev.to/theabbie/range-sum-query-2d-immutable-hna
"""
from typing import List
from itertools import accumulate


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # print(matrix)
        self.prefix_sum = [[] for _ in matrix]
        for row_idx, row in enumerate(matrix):
            for col_idx, val in enumerate(row):
                cur_cumulative_sum = val
                cur_cumulative_sum += self._get_val_on_prefix_sum(row_idx - 1, col_idx)
                cur_cumulative_sum += self._get_val_on_prefix_sum(row_idx, col_idx - 1)
                cur_cumulative_sum -= self._get_val_on_prefix_sum(row_idx - 1, col_idx - 1)
                self.prefix_sum[row_idx].append(cur_cumulative_sum)
        # print(self.prefix_sum)

    def _get_val_on_prefix_sum(self, row_idx: int, col_idx: int) -> int:
        if row_idx < 0 or col_idx < 0:
            return 0
        try:
            return self.prefix_sum[row_idx][col_idx]
        except IndexError:
            return 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_sum = self.prefix_sum[row2][col2]
        region_sum -= self._get_val_on_prefix_sum(row1 - 1, col2)
        region_sum -= self._get_val_on_prefix_sum(row2, col1 - 1)
        region_sum += self._get_val_on_prefix_sum(row1 - 1, col1 - 1)
        return region_sum


class NumMatrix2:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        a = map(accumulate, matrix)
        b = zip(*a)
        c = map(accumulate, b)
        d = zip(*c)
        e = list(map(list, d))
        self.prefixes = e

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top_sum = self.prefixes[row1 - 1][col2] if row1 > 0 else 0
        left_sum = self.prefixes[row2][col1 - 1] if col1 > 0 else 0
        origin = self.prefixes[row1 - 1][col1 - 1] if row1 != 0 and col1 != 0 else 0
        return self.prefixes[row2][col2] - top_sum - left_sum + origin


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
if __name__ == '__main__':
    test_input_matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    test_input_args = [2, 1, 4, 3]
    matrix = NumMatrix(test_input_matrix)
    print(matrix.sumRegion(*test_input_args))
    matrix2 = NumMatrix2(test_input_matrix)
    print(matrix2.sumRegion(*test_input_args))
