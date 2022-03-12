"""
https://leetcode.com/problems/copy-list-with-random-pointer
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """
    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        DICT: old_node_to_idx
        LIST: new_node[idx]
        """
        if not head:
            return

        node = head
        idx_by_node = {node: 0}
        cp_node_list = [Node(head.val)]

        idx = 0
        while node.next:
            node = node.next
            idx += 1
            idx_by_node[node] = idx
            cp_cur_node = Node(node.val)
            cp_node_list[-1].next = cp_cur_node
            cp_node_list.append(cp_cur_node)

        node = head
        idx = 0
        while node:
            try:
                cp_node_list[idx].random = cp_node_list[idx_by_node[node.random]]
            except KeyError:
                pass
            node = node.next
            idx += 1

        return cp_node_list[0]

    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        DICT: old_node_to_new_node
        """
        old_to_new = {None: None}

        node = head
        while node:
            old_to_new[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            cp_node = old_to_new[node]
            cp_node.next = old_to_new[node.next]
            cp_node.random = old_to_new[node.random]
            node = node.next

        return old_to_new[head]
