"""
https://leetcode.com/problems/queue-reconstruction-by-height/

> Topic: Math / Greedy Algorithm / Sorting / Segment Tree

Hint)
- What can you say about the position of the shortest person?
  If the position of the shortest person is i, how many people would be in front of the shortest person?
- Once you fix the position of the shortest person,
  what can you say about the position of the second shortest person?

Ref)
- https://www.youtube.com/watch?v=khddrw6Bfyw
- https://8iggy.tistory.com/138
- https://www.tutorialspoint.com/queue-reconstruction-by-height-in-cplusplus
- https://www.tutorialspoint.com/queue-reconstruction-by-height-in-javascript

[SEGMENT TREE]
- https://www.acmicpc.net/blog/view/9
- https://book.acmicpc.net/ds/segment-tree
"""
from typing import *


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for person in people:
            ans.insert(person[1], person)
        return ans


if __name__ == '__main__':
    sol = Solution()
    assert sol.reconstructQueue(
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    ) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
