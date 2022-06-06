"""
https://leetcode.com/problems/n-queens-ii/

> Topic: Backtracking / Bit Manipulation (bitset / bitmap / bitmask)

Ref)
- https://dev.to/seanpgallivan/solution-n-queens-ii-f08
- https://github.com/azl397985856/leetcode/blob/master/problems/52.N-Queens-II.md
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0

        def place(row_idx: int, vert: int, ldiag: int, rdiag: int) -> None:
            nonlocal ans

            if row_idx == n:
                ans += 1
                return

            for col_idx in range(n):
                vmask, lmask, rmask = 1 << col_idx, 1 << (row_idx + col_idx), 1 << (n - 1 + col_idx - row_idx)
                if vert & vmask or ldiag & lmask or rdiag & rmask:
                    continue

                place(row_idx + 1, vert | vmask, ldiag | lmask, rdiag | rmask)

        place(0, 0, 0, 0)
        return ans
