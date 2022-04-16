"""
https://leetcode.com/problems/convert-bst-to-greater-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    시간 복잡도: O(n)
    공간 복잡도: O(1)
    """
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        accumulated = 0

        def _convert_to_gst(node: TreeNode):
            nonlocal accumulated

            if node.right:
                _convert_to_gst(node.right)

            node.val += accumulated  # 중위 순회
            accumulated = node.val

            if node.left:
                _convert_to_gst(node.left)

        _convert_to_gst(root)
        return root
