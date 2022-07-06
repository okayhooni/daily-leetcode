"""
https://leetcode.com/problems/fibonacci-number/

> Topic: Dynamic Programming / Recursion /  Memoization / Tabulation / Math

Ref) https://dev.to/theabbie/fibonacci-number-do4
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a = 0
        b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
