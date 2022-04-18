"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

> Follow up: If the BST is modified often
(i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

1) https://www.baeldung.com/cs/kth-smallest-element-bst
   We can find the \boldsymbol{k}-th smallest element more efficiently,
   if we store into each node the number of its descendants.

2) https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/
   Augmented Tree Data Structure (O(h) Time Complexity and O(h) auxiliary space)
   The idea is to maintain the rank of each node.
   We can keep track of elements in the left subtree of every node while building the tree.
   Since we need the K-th smallest element, we can maintain the number of elements of the left subtree in every node.
   Assume that the root is having ‘lCount’ nodes in its left subtree. If K = lCount + 1, root is K-th node.
   If K < lCount + 1, we will continue our search (recursion) for the Kth smallest element in the left subtree of root.
   If K > lCount + 1, we continue our search in the right subtree for the (K – lCount – 1)-th smallest element.
   Note that we need the count of elements in the left subtree only.
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
    모든 풀이 공통

    시간 복잡도: O(n)
    공간 복잡도: O(h) = O(log(n))

    Morris Traversal 이용 시, 공간 복잡도를 O(1)로 줄일 수 있다.
    - https://www.geeksforgeeks.org/kth-smallest-element-in-bst-using-o1-extra-space/
    - https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur_k = 0

        def _inorder_visit_tree_until_k(node: Optional[TreeNode]) -> Optional[int]:
            nonlocal cur_k

            if not node:
                return

            left = _inorder_visit_tree_until_k(node.left)
            if left is not None:
                return left

            cur_k += 1
            if cur_k == k:
                return node.val

            right = _inorder_visit_tree_until_k(node.right)
            if right is not None:
                return right

        return _inorder_visit_tree_until_k(root)

    def kthSmallestWithStack(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            node = node.right
