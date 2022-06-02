"""
https://leetcode.com/problems/transpose-matrix/

Hint) We don't need any special algorithms to do this.
You just need to know what the transpose of a matrix looks like.
Rows become columns and vice versa!
"""
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_nums, col_nums = len(matrix), len(matrix[0])
        transposed = [[] for _ in range(col_nums)]

        for row in matrix:
            for col_idx, val in enumerate(row):
                transposed[col_idx].append(val)

        return transposed
