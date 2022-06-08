"""
https://leetcode.com/problems/remove-palindromic-subsequences/

> Topic: Two Pointers (Double Pointer)

Hint 1) Use the fact that string contains only 2 characters.
Hint 2) Are subsequences composed of only one type of letter always palindrome strings ?

Ref)
- https://dev.to/shivams136/leetcode-1332-remove-palindromic-subsequences-6dd
- https://dev.to/rohithv07/1332-remove-palindromic-subsequences-leetcode-easy-33ji
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return 2

            left += 1
            right -= 1

        return 1
