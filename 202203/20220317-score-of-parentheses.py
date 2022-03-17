"""
https://leetcode.com/problems/score-of-parentheses
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(n)
        """
        score_by_level_stack = []
        final_score = 0

        for char in s:
            if char == '(':
                score_by_level_stack.append(0)
            else:  # ')'
                cur_level_score = max(1, score_by_level_stack.pop())
                if score_by_level_stack:
                    score_by_level_stack[-1] += 2 * cur_level_score
                else:
                    final_score += cur_level_score

        return final_score

    def scoreOfParentheses_24ms_sample(self, S):
        """
        시간 복잡도: O(n)
        공간 복잡도: O(n)

        2 * multiplier 조건에 대한 처리: cur += stack.pop() + max(cur, 1)
        """
        stack, cur = [], 0
        for i in S:
            if i == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        return cur

    def scoreOfParentheses_21ms_sample(self, s: str) -> int:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(1)
        """
        points = 1
        total = 0
        for i, b in enumerate(s):
            if b == '(':
                points *= 2
            elif s[i - 1:i + 1] == '()':
                total = total + points // 2
                points //= 2
            elif b == ')':
                points //= 2
        return total


if __name__ == '__main__':
    sol = Solution()
    print(sol.scoreOfParentheses('((()))'))
    print(sol.scoreOfParentheses_24ms_sample('((()))'))
    print(sol.scoreOfParentheses_21ms_sample('((()))'))
