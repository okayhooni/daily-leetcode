"""
https://leetcode.com/problems/longest-palindromic-substring/

cf)
- https://leetcode.com/problems/palindromic-substrings/
- https://leetcode.com/problems/longest-palindromic-subsequence/

> Topic: Dynamic Programming / Two Pointer & Sliding Window

Hint 1) How can we reuse a previously computed palindrome to compute a larger palindrome?
Hint 2) If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
Hint 3) Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome,
we have O(n^2) start - end pairs and O(n) palindromic checks.
Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

Ref)
- https://github.com/azl397985856/leetcode/blob/master/problems/5.longest-palindromic-substring.md
- https://github.com/azl397985856/leetcode/blob/master/problems/516.longest-palindromic-subsequence.md

>>> max('z', 'aa')
'z'
>>> max('z', 'aa', key=len)
'aa'
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time Complexity: O(N ** 2)
        (Extra) Space Complexity: O(1)
        """

        def _get_palindrome_from_center(center_left_idx: int, center_right_idx: int) -> str:
            left_idx, right_idx = center_left_idx, center_right_idx

            while 0 <= left_idx and right_idx < len(s) and s[left_idx] == s[right_idx]:
                left_idx -= 1
                right_idx += 1

            return s[left_idx + 1:right_idx]

        longest = ''

        for center_idx in range(len(s)):
            longest = max(
                longest,
                _get_palindrome_from_center(center_idx - 1, center_idx),
                _get_palindrome_from_center(center_idx, center_idx),
                key=len
            )

        return longest

    def longestPalindromeWithDP(self, s: str) -> str:
        """
        Time Complexity: O(N ** 2)
        (Extra) Space Complexity: O(N ** 2)
        """
        if len(set(s)) == 1:
            return s

        dp = [[False] * len(s) for _ in range(len(s))]
        longest_palindrome_idx_pair = (0, 0)

        # dp[start][end] = True or False
        for idx in range(len(s)):
            dp[idx][idx] = True

        for idx in range(len(s) - 1):
            if s[idx] == s[idx + 1]:
                dp[idx][idx+1] = True
                longest_palindrome_idx_pair = max(
                    longest_palindrome_idx_pair,
                    (idx, idx + 1),
                    key=lambda pairs: pairs[1] - pairs[0]
                )

        # for start in range(len(s) - 2):
        #     for end in range(start + 1, len(s)):  # False ~> substring length is not bound on previous loop
        for end in range(2, len(s)):
            for start in range(end - 1):
                if s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = True
                    longest_palindrome_idx_pair = max(
                        longest_palindrome_idx_pair,
                        (start, end),
                        key=lambda pairs: pairs[1] - pairs[0]
                    )

        return s[longest_palindrome_idx_pair[0]:longest_palindrome_idx_pair[1] + 1]


if __name__ == '__main__':
    # test_case = "babad"
    test_case = "cbbd"
    sol = Solution()
    print(sol.longestPalindrome(test_case))
    print(sol.longestPalindromeWithDP(test_case))
