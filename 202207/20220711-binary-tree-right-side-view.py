"""
https://leetcode.com/problems/binary-tree-right-side-view/

> Topic: Tree / Binary Tree / DFS (Depth-First Search) / BFS (Breadth-First Search)

Ref)
- https://dev.to/seanpgallivan/solution-binary-tree-right-side-view-1kj1
- https://dev.to/cod3pineapple/199-binary-tree-right-side-view-44ii
"""
from typing import *
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res_rightmost = []
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res_rightmost.append(node.val)

        return res_rightmost

    def rightSideViewDfs(self, root: Optional[TreeNode]) -> List[int]:
        res_rightmost = []

        def dfs(node: TreeNode, level: int):
            if not node:
                return

            if len(res_rightmost) <= level:
                res_rightmost.append(node.val)
            else:
                res_rightmost[level] = node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return res_rightmost
