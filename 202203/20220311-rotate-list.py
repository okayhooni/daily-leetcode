"""
https://leetcode.com/problems/rotate-list
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    시간 복잡도: O(n)
    공간 복잡도: O(1)
    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        last_node = node = head
        list_len = 0

        while node:
            list_len += 1
            last_node = node
            node = node.next

        offset = k % list_len

        if offset:
            res_last = head

            for _ in range(list_len - offset - 1):
                res_last = res_last.next

            res_first = res_last.next
            res_last.next = None
            last_node.next = head
            return res_first
        else:
            return head
