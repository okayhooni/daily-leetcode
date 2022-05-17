"""
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

> Follow up: Could you solve the problem if repeated values on the tree are allowed?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(original_node, cloned_node):
            if original_node is None:
                return

            if original_node is target:
                return cloned_node

            target_in_left_cloned = dfs(original_node=original_node.left, cloned_node=cloned_node.left)
            if target_in_left_cloned:
                return target_in_left_cloned

            target_in_right_cloned = dfs(original_node=original_node.right, cloned_node=cloned_node.right)
            if target_in_right_cloned:
                return target_in_right_cloned

        return dfs(original_node=original, cloned_node=cloned)

    def getTargetCopyWithStack(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]

        while stack:
            original_node, cloned_node = stack.pop()

            if original_node is target:
                return cloned_node

            if original_node.left:
                stack.append((original_node.left, cloned_node.left))

            if original_node.right:
                stack.append((original_node.right, cloned_node.right))
