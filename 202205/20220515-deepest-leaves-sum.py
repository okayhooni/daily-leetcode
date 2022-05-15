"""
https://leetcode.com/problems/deepest-leaves-sum/

cf) https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        cur_depth_sum = None

        while queue:
            cur_depth_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                cur_depth_sum += node.val

        return cur_depth_sum
