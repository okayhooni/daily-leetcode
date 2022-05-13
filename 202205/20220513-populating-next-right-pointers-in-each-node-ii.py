"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

> Follow-up:
You may only use constant extra space.
The recursive approach is fine.
You may assume implicit stack space does not count as extra space for this problem.
"""
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        queue = deque([root])

        prev_node = None

        while queue:
            if prev_node:
                prev_node.next = None
                prev_node = None

            for _ in range(len(queue)):
                node = queue.popleft()
                if prev_node:
                    prev_node.next = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                prev_node = node

        return root
