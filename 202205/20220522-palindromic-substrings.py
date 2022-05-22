"""
https://leetcode.com/problems/palindromic-substrings/

cf) https://leetcode.com/problems/longest-palindromic-substring/

> Topic: Dynamic Programming / Two Pointer & Sliding Window

> Hint:
- How can we reuse a previously computed palindrome to compute a larger palindrome?
- If “aba” is a palindrome, is “xabax” and palindrome? Similarly is “xabay” a palindrome?
- Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome,
we have O(n^2) start - end pairs and O(n) palindromic checks.
Can we reduce the time for palindromic checks to O(1) by reusing some previous computation?
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromic_substr_cnt = 0

        def expand(left: int, right: int):
            nonlocal palindromic_substr_cnt

            while 0 <= left and right < len(s) and s[left] == s[right]:
                palindromic_substr_cnt += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return palindromic_substr_cnt

    def countSubstringsWithDP(self, s: str) -> int:
        count = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        # dp[start][end] = True or False
        for idx in range(len(s)):
            dp[idx][idx] = True
            count += 1

        for idx in range(len(s) - 1):
            if s[idx] == s[idx + 1]:
                dp[idx][idx+1] = True
                count += 1

        # for start in range(len(s) - 2):
        #     for end in range(start + 1, len(s)):  # False ~> substring length is not bound on previous loop
        for end in range(2, len(s)):
            for start in range(end - 1):
                if s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = True
                    count += 1

        return count
