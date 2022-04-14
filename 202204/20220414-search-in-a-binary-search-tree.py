"""
https://leetcode.com/problems/search-in-a-binary-search-tree/
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
    시간 복잡도: O(log(n))
    공간 복잡도: O(1)
    """
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root

        while node:
            if node.val < val:
                node = node.right
            elif node.val > val:
                node = node.left
            else:
                return node
