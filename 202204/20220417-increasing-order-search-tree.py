"""
https://leetcode.com/problems/increasing-order-search-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        res = f'TreeNode: val: {self.val}'
        if self.left:
            res += f' / left: {self.left.val}'
        if self.right:
            res += f' / right: {self.right.val}'
        return res


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(n)
    공간 복잡도: O(1)
    """
    def increasingBST(self, root: TreeNode) -> Optional[TreeNode]:
        """재귀 풀이"""
        prev_node = None
        new_root_node = None

        def _visit_inorder(node: TreeNode):
            nonlocal prev_node, new_root_node

            if not node:
                return

            _visit_inorder(node.left)

            if not prev_node:
                new_root_node = prev_node = node
            else:
                # prev_node.left = None
                prev_node.right = node
                node.left = None
                prev_node = node

            _visit_inorder(node.right)

        _visit_inorder(root)

        return new_root_node

    def increasingBST2(self, root: TreeNode) -> Optional[TreeNode]:
        """반복 풀이"""
        node = root
        stack = []
        new_root_node, prev_node = None, None

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if not prev_node:
                new_root_node = prev_node = node
            else:
                # prev_node.left = None
                prev_node.right = node
                node.left = None
                prev_node = node

            node = node.right

        return new_root_node

    def increasingBST_23ms_sol(self, root: Optional[TreeNode], tail: Optional[TreeNode] = None) -> Optional[TreeNode]:
        """우아하네"""
        if not root:
            return tail

        res = self.increasingBST_23ms_sol(root.left, root)
        root.left = None
        root.right = self.increasingBST_23ms_sol(root.right, tail)

        return res


if __name__ == '__main__':
    # [2, 1, 4, None, None, 3]
    root_node = TreeNode(2, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3)))
    sol = Solution()

    print_node = sol.increasingBST(root_node)

    while print_node.right:
        print(print_node)
        print_node = print_node.right
