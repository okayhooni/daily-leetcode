"""
https://leetcode.com/problems/binary-search-tree-iterator/

Follow up:
Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory,
where h is the height of the tree?
"""
from typing import Optional, Generator
from inspect import getgeneratorstate


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.node_gen = self._inorder_traverse(root)
        self.tmp_next = None

    def _inorder_traverse(self, node: Optional[TreeNode]) -> Generator[int, None, None]:
        stack = []

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            yield node.val
            node = node.right

    def next(self) -> Optional[int]:
        """
        시간 복잡도: O(h)
        공간 복잡도: O(h)
        """
        if self.tmp_next is not None:
            tmp = self.tmp_next
            self.tmp_next = None
            return tmp

        try:
            return next(self.node_gen)
        except StopIteration:
            return None

    def hasNext(self) -> bool:
        """
        시간 복잡도: O(1)
        """
        if self.tmp_next is not None:
            return True

        # print(getgeneratorstate(self.node_gen))
        try:
            self.tmp_next = next(self.node_gen)
        except StopIteration:
            return False
        else:
            return True


class BSTIterator51msSol:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        self.push(root)

    def next(self) -> int:
        """
        시간 복잡도: O(h)
        공간 복잡도: O(h)
        """
        temp = self.stack.pop()
        self.push(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        """
        시간 복잡도: O(1)
        """
        return bool(self.stack)

    def push(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
if __name__ == '__main__':
    tr = TreeNode(
        3,
        left=TreeNode(1),
        right=TreeNode(4, left=TreeNode(2))
    )
    it = BSTIterator(tr)
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.hasNext())
    print(it.next())
