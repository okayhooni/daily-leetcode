"""
https://leetcode.com/problems/valid-parentheses
"""


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """

    STACK_PAIR_MAP = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in self.STACK_PAIR_MAP:
                stack.append(char)
            elif not stack or char != self.STACK_PAIR_MAP[stack.pop()]:
                return False

        return len(stack) == 0

    ####################################################################

    STACK_PAIR_MAP_2 = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    def isValid2(self, s: str) -> bool:
        """
        역매핑
        """
        stack = []

        for char in s:
            if char in self.STACK_PAIR_MAP:
                if not stack or stack.pop() != self.STACK_PAIR_MAP[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

    ####################################################################

    BRACKETS_MAPPER = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    def isValid3(self, s: str) -> bool:
        """
        기억은 없지만 서브밋 기록이 있는 풀이
        """
        stack = []
        try:
            for char in s:
                if char in self.BRACKETS_MAPPER:
                    stack.append(char)
                elif char == self.BRACKETS_MAPPER[stack[-1]]:
                    stack.pop()
                else:
                    return False

            return False if stack else True
        except IndexError:
            return False
