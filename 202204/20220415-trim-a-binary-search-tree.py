"""
https://leetcode.com/problems/trim-a-binary-search-tree/
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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        내 풀이 코드가 36ms solution 코드보다 분기가 더 많아서 코드는 깔끔해보이지 않지만,
        root.val == low 인 케이스와, root.val == high 인 케이스에 가지치기가 더 빨리 되어,
        극단적인 케이스의 인풋에 대해 더 효율적이다
        """
        if not root:
            return

        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val == low:
            root.left = None
            root.right = self.trimBST(root.right, low, high)
            return root
        elif low < root.val < high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        elif root.val == high:
            root.left = self.trimBST(root.left, low, high)
            root.right = None
            return root
        else:  # root.val > high
            return self.trimBST(root.left, low, high)

    def trimBST_36ms_sol(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        종단 조건 + 3가지 분기로 깔끔한 풀이 가능
        """
        if not root:
            return None
        if root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low:
            return self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
