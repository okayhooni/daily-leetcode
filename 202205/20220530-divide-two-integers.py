"""
https://leetcode.com/problems/divide-two-integers/

> Topic: Bit Manipulation, Math (log)

Ref)
- https://dev.to/seanpgallivan/solution-divide-two-integers-5dcd
- https://dev.to/seanpgallivan/solution-divide-two-integers-ver-2-26pp
- https://github.com/azl397985856/leetcode/blob/master/problems/29.divide-two-integers.md

we can use bit manipulation to simulate multiplication/division.
Since a bitwise shift to the left is the equivalent of a multiplication by 2,
if we count how many times we can bitwise shift B to the left while still staying under A,
then we can quickly work out a chunk of the solution.

All that's left is to start over with the remaining amount of A and repeat this process,
adding the results to our answer (ans) as we go.

Of course, negative numbers will play havoc with our bitwise shifting,
so we should first extract the sign difference and then use only positive numbers for A and B.
"""
import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        res, mod = divmod(dividend, divisor)
        return res + 1 if res < 0 and mod else res

    def divide_bitwise(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        ans, sign = 0, 1
        if dividend < 0:
            dividend, sign = -dividend, -sign
        if divisor < 0:
            divisor, sign = -divisor, -sign

        if dividend == divisor:
            return sign

        while dividend >= divisor:
            b = 0

            while dividend >= (divisor << (b + 1)):
                b += 1

            dividend -= (divisor << b)
            ans += (1 << b)

        return -ans if sign < 0 else ans

    def divide_log_math(self, dividend: int, divisor: int) -> int:  # False
        if dividend == 0:
            return 0

        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        ans = math.floor(math.exp(math.log(abs(dividend)) - math.log(abs(divisor))))
        return ans if dividend * divisor > 0 else -ans
