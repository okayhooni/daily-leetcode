"""
https://leetcode.com/problems/binary-tree-cameras/

> Topic: Dynamic Programming / DFS (Depth-First Search)

Ref) https://dev.to/seanpgallivan/solution-binary-tree-cameras-1a5i

we never need to place a camera on a leaf, since it would always be better to place a camera on the node above a leaf.
This should lead us to thinking that we need to start from the bottom of the binary tree and work our way up.

This naturally calls for a depth first search (DFS) approach with a recursive helper function (dfs).
We can navigate to the lowest part of the tree, then deal with placing cameras on the way back up the recursion stack,
using the return values to pass information from child to parent.
"""
from enum import IntEnum
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeMonitorStatus(IntEnum):
    NULL = 0
    MONITORED = 0
    CAMERA = 1
    UNMONITORED = 3


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(N) where N is the number of nodes in the binary tree
        (Extra) Space Complexity: O(M) where M is the maximum depth of the binary tree,
                                  which can range up to N, for the recursion stack
        """
        ans = 0

        def dfs(node: TreeNode) -> int:
            nonlocal ans

            if not node:
                return NodeMonitorStatus.NULL

            val = dfs(node.left) + dfs(node.right)
            if 0 < val <= (NodeMonitorStatus.CAMERA + NodeMonitorStatus.CAMERA):
                return NodeMonitorStatus.MONITORED
            if val == 0:
                return NodeMonitorStatus.UNMONITORED

            ans += 1
            return NodeMonitorStatus.CAMERA

        return ans + 1 if dfs(root) == NodeMonitorStatus.UNMONITORED else ans
