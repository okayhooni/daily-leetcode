"""
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(n)
        """
        res = ''
        residual = k

        for i in range(n):
            cur_opti_min = max(residual - 26 * (n - 1 - i), 1)

            res += chr(ord('a') + cur_opti_min - 1)
            residual -= cur_opti_min

        return res

    def getSmallestString_24ms_sample(self, n: int, k: int) -> str:
        """
        시간 복잡도: O(1)
        공간 복잡도: O(n)
        """
        diff = k - n  # sum(1, 1, 1, 1, 1, 1, ~, 1) = n
        quotient = diff // 25  # = (26 - 1)
        reminder = diff % 25
        ans = "a" * (n-quotient-1) + chr(97+reminder) + "z" * quotient if reminder \
            else "a" * (n-quotient) + "z" * quotient
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getSmallestString(92170, 99288))
