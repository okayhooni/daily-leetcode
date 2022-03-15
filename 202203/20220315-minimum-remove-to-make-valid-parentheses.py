"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses
"""


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """
    @staticmethod
    def validate_str(s: str, begin_char: str = '(', end_char: str = ')') -> str:
        begin_parentheses = []
        res_str = ''

        for char in s:
            if char == end_char:
                try:
                    begin_parentheses.pop()
                except IndexError:
                    pass
                else:
                    res_str += char
                finally:
                    continue

            res_str += char
            if char == begin_char:
                begin_parentheses.append(char)

        return res_str

    def minRemoveToMakeValid1(self, s: str) -> str:
        intermediate_str = self.validate_str(s, '(', ')')
        reversed_res_str = self.validate_str(intermediate_str[::-1], ')', '(')
        return reversed_res_str[::-1]

    def minRemoveToMakeValid2(self, s: str) -> str:
        char_seq = list(s)
        open_paren_idx_stack = []

        for idx, char in enumerate(char_seq):
            if char == '(':
                open_paren_idx_stack.append(idx)
            elif char == ')':
                try:
                    open_paren_idx_stack.pop()
                except IndexError:
                    char_seq[idx] = ''

        for remaining_open_paren_idx in open_paren_idx_stack:
            char_seq[remaining_open_paren_idx] = ''

        return ''.join(char_seq)
