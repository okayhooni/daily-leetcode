"""
https://leetcode.com/problems/maximum-frequency-stack

파이썬 알고리즘 인터뷰 서적 관련 문제)
p.308 : 상위 K 빈도 요소(최소힙의 음수화)
"""
from collections import Counter
from heapq import heappush, heappop


class FreqStack:

    def __init__(self):
        self.counter = Counter()
        self.heap = []
        self.pushed_idx = 0

    def push(self, val: int) -> None:
        """
        시간 복잡도: O(log(n))
        공간 복잡도: O(n)
        """
        self.counter[val] += 1
        # heappush(self.heap, (-self.counter[val], -len(self.heap), val))
        heappush(self.heap, (-self.counter[val], -self.pushed_idx, val))
        self.pushed_idx += 1

    def pop(self) -> int:
        """
        시간 복잡도: O(1)
        """
        # print(self.heap)
        *_, val = heappop(self.heap)
        self.counter[val] -= 1
        # print(val)
        return val


class FreqStackWithNoHeap:
    """
    REF: 272ms submission
    힙 구조 유지가 필요없으므로 더 효율적인 push 가능
    """

    def __init__(self):
        self.counter = Counter()
        self.stack_by_freq_stack = []

    def push(self, val: int) -> None:
        """
        시간 복잡도: O(1)
        공간 복잡도: O(n)
        """
        # 하나씩만 push 되므로
        if len(self.stack_by_freq_stack) == self.counter[val]:
            self.stack_by_freq_stack.append([])

        self.stack_by_freq_stack[self.counter[val]].append(val)
        self.counter[val] += 1

    def pop(self) -> int:
        """
        시간 복잡도: O(1)
        """
        val = self.stack_by_freq_stack[-1].pop()
        if not self.stack_by_freq_stack[-1]:
            self.stack_by_freq_stack.pop()

        self.counter[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
if __name__ == '__main__':
    fs = FreqStack()

    cmd = [
        "push", "push", "push", "push", "push", "push", "pop",
        "push", "pop", "push", "pop", "push", "pop",
        "push", "pop", "pop", "pop", "pop", "pop", "pop"
    ]

    args = [[4], [0], [9], [3], [4], [2], [], [6], [], [1], [], [1], [], [4], [], [], [], [], [], []]

    for c, a in zip(cmd, args):
        getattr(fs, c)(*a)
