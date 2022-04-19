"""
https://leetcode.com/problems/recover-binary-search-tree/

> Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
- https://afteracademy.com/blog/recover-binary-search-tree
- https://www.geeksforgeeks.org/fix-two-swapped-nodes-of-bst/
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(1)

        Do not return anything, modify root in-place instead.
        """

        prev_node = None
        target_node = None

        def _inorder_visit_tree(node: Optional[TreeNode]):
            nonlocal prev_node, target_node

            if not node:
                return

            _inorder_visit_tree(node.left)

            if prev_node and not target_node and prev_node.val > node.val:
                target_node = prev_node
                prev_node = node
            elif target_node and target_node.val < node.val:
                raise Exception
            else:
                prev_node = node

            _inorder_visit_tree(node.right)

        try:
            _inorder_visit_tree(root)
        except:
            pass
        finally:
            prev_node.val, target_node.val = target_node.val, prev_node.val


if __name__ == '__main__':
    tr = TreeNode(
        3,
        left=TreeNode(1),
        right=TreeNode(4, left=TreeNode(2))
    )
    sol = Solution()
    sol.recoverTree(tr)
