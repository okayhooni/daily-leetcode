"""
https://leetcode.com/problems/n-queens/

> Topic: Backtracking / Bit Manipulation (bitset / bitmap / bitmask)

Ref)
- https://dev.to/wanguiwaweru/n-queens-4ic1
- https://dev.to/seanpgallivan/solution-n-queens-5hdb
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        occupied_columns_vertical = []  # keep track of the columns
        occupied_positive_diagonal = []  # row+column
        occupied_negative_diagonal = []  # row-column
        ans = []  # final result
        board = [['.'] * n for i in range(n)]  # initialize board with 0 in all rows

        def backtrack(row):
            if row == n:  # all rows have been visited
                copied = [''.join(row) for row in board]
                ans.append(copied)
                return

            for col in range(n):
                if col in occupied_columns_vertical \
                        or (row + col) in occupied_positive_diagonal \
                        or (row - col) in occupied_negative_diagonal:
                    continue  # cannot place a queen in this position

                # update the variables we are keeping track of
                occupied_columns_vertical.append(col)
                occupied_positive_diagonal.append(row + col)
                occupied_negative_diagonal.append(row - col)
                board[row][col] = 'Q'

                backtrack(row + 1)  # move to next row and

                # occupied_columns_vertical.remove(col)
                # occupied_positive_diagonal.remove(row + col)
                # occupied_negative_diagonal.remove(row - col)
                occupied_columns_vertical.pop()
                occupied_positive_diagonal.pop()
                occupied_negative_diagonal.pop()
                board[row][col] = '.'

        backtrack(0)  # call the function
        return ans

    def solveNQueensBitwise(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.'] * n for _ in range(n)]

        def place(row_idx: int, vert: int, ldiag: int, rdiag: int) -> None:
            if row_idx == n:
                ans.append(["".join(row) for row in board])
                return
            for col_idx in range(n):
                vmask = 1 << col_idx
                lmask = 1 << (row_idx + col_idx)
                # rmask = 1 << (n - 1 + col_idx - row_idx)  # OK
                rmask = 1 << (n - 1 + row_idx - col_idx)  # OK

                if vert & vmask or ldiag & lmask or rdiag & rmask:
                    continue

                board[row_idx][col_idx] = 'Q'
                place(row_idx + 1, vert | vmask, ldiag | lmask, rdiag | rmask)
                board[row_idx][col_idx] = '.'

        place(0, 0, 0, 0)
        return ans
