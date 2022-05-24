"""
https://leetcode.com/problems/longest-valid-parentheses/

> Topic: Dynamic Programming / Stack

cf) 20220315-minimum-remove-to-make-valid-parentheses
- https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

Ref)
- https://dev.to/seanpgallivan/solution-longest-valid-parentheses-592n
- https://github.com/azl397985856/leetcode/blob/master/problems/32.longest-valid-parentheses.md

Since we stored the index of the '(' in our stack,
we can easily find the difference between the ')' at i and the last entry in the stack,
which should be the length of the valid substring which was just closed.

But here we run into a problem,
because consecutive valid substrings can be grouped into a larger valid substring (ie, '()()' = 4).
So instead of counting from the last stack entry,
we should actually count from the second to last entry,
to include any other valid closed substrings [= exists on the same layer with the just-matched last stack entry.]
since the most recent '(' that will still remain after we pop the just-matched last stack entry off.

This, of course, brings us to the second and third changes.
Since we're checking the second to last stack entry,
what happens in the case of '()()'
when you close the second valid substring yet there's only the one stack entry left at the time?

To avoid this issue,
we can just wrap the entire string in another imaginary set of parentheses by starting with stack = [-1],
indicating that there's an imaginary '(' just before the beginning of the string at i = 0.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def check_longest_from_begin(string: str, begin_char: str = '('):
            tmp_ans = begin_cnt = end_cnt = 0

            for char in string:
                if char == begin_char:
                    begin_cnt += 1
                else:
                    end_cnt += 1

                if begin_cnt < end_cnt:
                    begin_cnt = end_cnt = 0
                elif begin_cnt == end_cnt:
                    tmp_ans = max(tmp_ans, begin_cnt + end_cnt)

            return tmp_ans

        return max(
            check_longest_from_begin(s, '('),
            check_longest_from_begin(s[::-1], ')')
        )

    def longestValidParenthesesWithStack(self, s: str) -> int:
        stack, ans = [], 0
        cur_valid_first_start_idx = 0
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            else:  # ')'
                try:
                    _ = stack.pop()
                except IndexError:
                    cur_valid_first_start_idx = idx + 1
                else:
                    if stack:
                        cur_start_idx = stack[-1] + 1
                    else:
                        cur_start_idx = cur_valid_first_start_idx

                    ans = max(ans, idx - cur_start_idx + 1)

            print(f'stack: {stack} / cur_valid_first_start_idx: {cur_valid_first_start_idx} / ans: {ans}')

        return ans

    def longestValidParenthesesRefStackSolution(self, s: str) -> int:
        stack, ans = [-1], 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif len(stack) == 1:
                stack[0] = i
            else:
                stack.pop()
                ans = max(ans, i - stack[-1])
        return ans

    def longestValidParenthesesWithDP(self, s: str) -> int:
        ans = 0
        dp = [0] * len(s)  # (slen + 1)
        for idx, char in enumerate(s):
            if char == '(':
                continue

            # ')'
            left_paren = idx - 1 - dp[idx - 1]  # dp[idx - 1] ~ considering nested brackets
            if left_paren >= 0 and s[left_paren] == '(':
                dp[idx] = dp[idx - 1] + 2

                if idx - dp[idx] >= 0:
                    dp[idx] += dp[idx - dp[idx]]  # dp[idx - dp[idx] ~ considering brackets on the same layer

                ans = max(ans, dp[idx])

            print(dp)

        return ans

    def longestValidParenthesesRefDPSolution(self, s: str) -> int:
        mlen = 0
        slen = len(s)
        dp = [0] * (slen + 1)
        for i in range(1, len(s) + 1):

            if s[i - 1] == '(':
                continue

            left_paren = i - 2 - dp[i - 1]
            if left_paren >= 0 and s[left_paren] == '(':
                dp[i] = dp[i - 1] + 2

                if dp[i - dp[i]]:
                    dp[i] += dp[i - dp[i]]

                if dp[i] > mlen:
                    mlen = dp[i]

        return mlen


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses("(()"))
    print(sol.longestValidParentheses("()(()"))
    print(sol.longestValidParentheses("()(()("))
    print(sol.longestValidParentheses("(())"))
    print(sol.longestValidParentheses("(())()"))
    print(sol.longestValidParentheses("(())())"))
    print(sol.longestValidParentheses("()(()"))
    print(sol.longestValidParentheses("()(())"))
    print(sol.longestValidParentheses("(()()"))
    print(sol.longestValidParentheses(")))()"))
    print(sol.longestValidParentheses("()((()))(())"))
    print(sol.longestValidParentheses("(()((()))(())"))
    print(sol.longestValidParentheses("((()((()))(())"))
    print(sol.longestValidParentheses("(((()((()))(())"))
    print(sol.longestValidParentheses("()((()))((()(())))"))
    print(sol.longestValidParentheses("(((()((()))((()(())))"))
    print(sol.longestValidParenthesesWithDP("()((()))((()(())))"))
    print(sol.longestValidParenthesesWithDP("()()((()))((()(())))"))
    print(sol.longestValidParenthesesWithDP("()"))
