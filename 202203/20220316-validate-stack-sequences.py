"""
https://leetcode.com/problems/validate-stack-sequences
"""
from typing import List


class Solution:
    """
    시간 복잡도: O(n) : stack이 채워져야만 내부 loop을 수행하므로, 상한이 O(n^2)이 아닌 O(n)
    공간 복잡도: O(n)
    """
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_idx = 0

        for element in pushed:
            stack.append(element)
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1

        return len(stack) == 0
