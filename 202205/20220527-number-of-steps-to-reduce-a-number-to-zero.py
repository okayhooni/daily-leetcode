"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

> Topic: Bit Manipulation
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num > 0:
            div, mod = divmod(num, 2)
            if mod:
                num -= 1
            else:
                num = div

            cnt += 1

        return cnt

    def numberOfStepsBitwise(self, num: int) -> int:
        cnt = 0
        while num > 0:
            if num % 2:
                num -= 1
            else:
                num >>= 1

            cnt += 1

        return cnt


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSteps(123))
    print(sol.numberOfStepsBitwise(123))
