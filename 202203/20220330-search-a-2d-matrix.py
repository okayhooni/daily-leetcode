"""
https://leetcode.com/problems/search-a-2d-matrix/
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(1)
        """
        for row in matrix:
            if target <= row[-1]:
                return target in row

        return False

    def searchMatrixWithBinarySearch(self, matrix: List[List[int]], target: int) -> bool:
        """
        시간 복잡도: O(log(n))
        공간 복잡도: O(1)
        """
        row_cnt, col_cnt = len(matrix), len(matrix[0])

        left = 0
        right = row_cnt * col_cnt - 1

        while left <= right:
            mid = (left + right) // 2
            cur_row_idx, cur_col_idx = divmod(mid, col_cnt)
            cur_num = matrix[cur_row_idx][cur_col_idx]

            if cur_num == target:
                return True
            elif target < cur_num:
                right = mid - 1
            elif target > cur_num:
                left = mid + 1

        return False
