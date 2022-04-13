"""
https://leetcode.com/problems/spiral-matrix-ii/
"""
from typing import List


class Solution:
    """
    N = n**2

    시간 복잡도: O(N)
    공간 복잡도: O(N)
    """
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]

        cur_n = 1
        cur_low_bound, cur_high_bound = 0, n - 1
        cur_horizon_jdx, cur_vertical_idx = 0, 0
        max_n = n ** 2

        # while cur_low_bound <= cur_high_bound:
        while cur_n <= max_n:
            res[cur_vertical_idx][cur_horizon_jdx] = cur_n

            cur_n += 1
            if cur_horizon_jdx < cur_high_bound and cur_vertical_idx == cur_low_bound:
                cur_horizon_jdx += 1
            elif cur_horizon_jdx == cur_high_bound and cur_vertical_idx < cur_high_bound:
                cur_vertical_idx += 1
            elif cur_low_bound < cur_horizon_jdx and cur_vertical_idx == cur_high_bound:
                cur_horizon_jdx -= 1
            elif cur_horizon_jdx == cur_low_bound and cur_low_bound + 1 < cur_vertical_idx:
                cur_vertical_idx -= 1
            else:
                cur_horizon_jdx += 1
                cur_low_bound += 1
                cur_high_bound -= 1

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(3))
    print(sol.generateMatrix(4))
