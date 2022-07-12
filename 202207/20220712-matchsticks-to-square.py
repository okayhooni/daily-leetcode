"""
https://leetcode.com/problems/matchsticks-to-square/

> Topic: Dynamic Programming / Backtracking / Bit Manipulation / Bitmask

Hint)
- Treat the matchsticks as an array. Can we split the array into 4 equal halves?
- Every matchstick can belong to either of the 4 sides. We don't know which one. Maybe try out all options!
- For every matchstick, we have to try out each of the 4 options i.e. which side it can belong to.
  We can make use of recursion for this.
- We don't really need to keep track of which matchsticks belong to a particular side during recursion.
  We just need to keep track of the length of each of the 4 sides.
- When all matchsticks have been used we simply need to see the length of all 4 sides.
  If they're equal, we have a square on our hands!

Ref)
- https://dev.to/seanpgallivan/solution-matchsticks-to-square-2fk8
- https://github.com/walkccc/LeetCode/blob/main/solutions/0473.%20Matchsticks%20to%20Square/0473.py
"""
from typing import *
from functools import cache


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        Time Complexity: O(2^N) where N is the length of M for the attempted combinations of elements in M
        Space Complexity: O(N) for the recursion stack
        """
        n, side = len(matchsticks), sum(matchsticks) / 4
        matchsticks.sort(reverse=True)
        if side != int(side) or matchsticks[0] > side:
            return False

        def btrack(i, space, done):
            if done == 3:
                return True
            while i < n:
                num = matchsticks[i]
                if num > space:
                    i += 1
                    continue
                matchsticks[i] = side + 1
                if num == space:
                    res = btrack(1, side, done+1)
                else:
                    res = btrack(i+1, space-num, done)
                if res:
                    return True
                matchsticks[i] = num
                while i < n and matchsticks[i] == num:
                    i += 1
            return False
        return btrack(0, side, 0)

    def makesquareTimeLimitExceeded(self, matchsticks: List[int]) -> bool:
        @cache
        def dfs(idx: int, left: int, right: int, top: int, bottom: int):
            if idx == len(matchsticks):
                return left == right == top == bottom

            cur_stick = matchsticks[idx]

            if dfs(idx + 1, left + cur_stick, right, top, bottom):
                return True
            if dfs(idx + 1, left, right + cur_stick, top, bottom):
                return True
            if dfs(idx + 1, left, right, top + cur_stick, bottom):
                return True
            if dfs(idx + 1, left, right, top, bottom + cur_stick):
                return True

            return False

        return dfs(0, 0, 0, 0, 0)


if __name__ == "__main__":
    sol = Solution()
    assert sol.makesquare([1, 1, 2, 2, 2])
