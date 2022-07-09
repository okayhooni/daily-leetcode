"""
https://leetcode.com/problems/interleaving-string/

> Topic: Dynamic Programming

> Follow up: Could you solve it using only O(s2.length) additional memory space?

Ref) https://dev.to/seanpgallivan/solution-interleaving-string-1497

If we consider a matrix with indices (i) for s1 on one axis and indices (j) for s2 on the other,
then a successful s3 can be considered a path moving from the top left to the bottom right.
At each point, we either move downward (i++) by choosing the next letter from s1
or rightward (j++) by choosing the next letter from s2.
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1) + 2, len(s2) + 2
        if n + m - 4 != len(s3): return False
        dp = [0] * m
        dp[1] = 1
        for i in range(1, n):
            for j in range(1, m):
                up = dp[j] and (i < 2 or s1[i-2] == s3[j+i-3])
                left = dp[j-1] and (j < 2 or s2[j-2] == s3[j+i-3])
                dp[j] = up or left
        return bool(dp[-1])


if __name__ == "__main__":
    sol = Solution()
    assert sol.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac")
