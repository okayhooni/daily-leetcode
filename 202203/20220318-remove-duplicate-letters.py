"""
https://leetcode.com/problems/remove-duplicate-letters
"""
from collections import Counter


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """

    def removeDuplicateLetters(self, s: str) -> str:
        """스택 기반 풀이"""
        stack = []
        handled_char_set = set()
        char_counter = Counter(s)

        for char in s:
            char_counter[char] -= 1

            if char in handled_char_set:
                continue

            while stack and stack[-1] > char and char_counter[stack[-1]] > 0:
                handled_char_set.remove(stack.pop())

            stack.append(char)
            handled_char_set.add(char)

        return ''.join(stack)

    def removeDuplicateLetters2(self, s: str) -> str:
        """재귀 기반 풀이"""
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(suffix) == set(s):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))

        return ''  # s = '' case
