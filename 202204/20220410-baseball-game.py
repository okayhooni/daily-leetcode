"""
https://leetcode.com/problems/baseball-game/
"""
from typing import List


class Solution:
    """
    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """
    def calPoints(self, ops: List[str]) -> int:
        # prev_points_queue = deque(maxlen=2)
        points = []

        for op in ops:
            if op == '+':
                points.append(sum(points[-2:]))
            elif op == 'D':
                points.append(points[-1] * 2)
            elif op == 'C':
                points.pop()
            else:
                points.append(int(op))

        return sum(points)


if __name__ == '__main__':
    sol = Solution()
    print(sol.calPoints(["36", "28", "70", "65", "C", "+", "33", "-46", "84", "C"]))
