"""
https://leetcode.com/problems/backspace-string-compare/
"""


class Solution:
    """
    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """
    @staticmethod
    def convert_string_with_stack(input_str: str) -> str:
        stack = []
        for char in input_str:
            if char == '#':
                try:
                    stack.pop()
                except IndexError:
                    pass
            else:
                stack.append(char)

        return ''.join(stack)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.convert_string_with_stack(s) == self.convert_string_with_stack(t)
