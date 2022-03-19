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
        self.counter[val] += 1
        # heappush(self.heap, (-self.counter[val], -len(self.heap), val))
        heappush(self.heap, (-self.counter[val], -self.pushed_idx, val))
        self.pushed_idx += 1

    def pop(self) -> int:
        # print(self.heap)
        *_, val = heappop(self.heap)
        self.counter[val] -= 1
        # print(val)
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
