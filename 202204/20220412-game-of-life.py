"""
https://leetcode.com/problems/game-of-life/
"""
from typing import List
from collections import Counter


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(n)
    공간 복잡도: O(1) : in-place

    Do not return anything, modify board in-place instead.

    Follow up:
    - Could you solve it in-place? Remember that the board needs to be updated simultaneously:
      You cannot update some cells first and then use their updated values to update other cells.
    - In this question, we represent the board using a 2D array.
      In principle, the board is infinite,
      which would cause problems when the active area encroaches upon the border of the array
      (i.e., live cells reach the border). How would you address these problems?
    """
    def gameOfLife(self, board: List[List[int]]) -> None:
        width, height = len(board[0]), len(board)

        def _convert_value_on_block(idx: int, jdx: int) -> None:
            neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

            living_neighbors_cnt = 0

            for idx_delta, jdx_delta in neighbors:
                neighbor_idx, neighbor_jdx = idx + idx_delta, jdx + jdx_delta

                if 0 <= neighbor_idx < width and 0 <= neighbor_jdx < height \
                        and board[neighbor_jdx][neighbor_idx] in {1, 2}:
                    living_neighbors_cnt += 1

            if living_neighbors_cnt < 2 or living_neighbors_cnt > 3:
                board[jdx][idx] = 2 if board[jdx][idx] == 1 else 0
            elif living_neighbors_cnt == 3 and board[jdx][idx] == 0:
                board[jdx][idx] = 3

        for vertical_jdx in range(height):
            for horizontal_idx in range(width):
                _convert_value_on_block(horizontal_idx, vertical_jdx)

        for vertical_jdx in range(height):
            for horizontal_idx in range(width):
                board[vertical_jdx][horizontal_idx] %= 2

    def gameOfLifeWithCounter(self, board: List[List[int]]) -> None:
        width_j, height_i = len(board[0]), len(board)
        living_idx_set = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        living_neigbor_counter = Counter(
            (target_i, target_j)
            for i, j in living_idx_set
            for target_i in range(i - 1, i + 2)
            for target_j in range(j - 1, j + 2)
            if (target_i != i or target_j != j) and 0 <= target_i < height_i and 0 <= target_j < width_j
        )

        for i in range(height_i):
            for j in range(width_j):
                cur_living_neighbor_cnt = living_neigbor_counter[i, j]

                if cur_living_neighbor_cnt == 3 or (cur_living_neighbor_cnt == 2 and (i, j) in living_idx_set):
                    board[i][j] = 1
                else:
                    board[i][j] = 0
