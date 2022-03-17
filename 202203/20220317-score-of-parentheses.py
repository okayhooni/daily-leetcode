"""
https://leetcode.com/problems/score-of-parentheses
"""


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """
    def scoreOfParentheses(self, s: str) -> int:
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


if __name__ == '__main__':
    sol = Solution()
    print(sol.scoreOfParentheses('((()))'))
    print(sol.scoreOfParentheses_24ms_sample('((()))'))
