"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

> Topic: Tree / Binary Tree / DFS (Depth-First Search) / BFS (Breadth-First Search)
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            cur_level = []
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                left, right = cur_node.left, cur_node.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)

                cur_level.append(cur_node.val)

            res.append(cur_level)

        return res
