"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(n)
    공간 복잡도: O(1)
    """
    @staticmethod
    def _get_list_len(head: ListNode) -> int:
        node = head
        list_len = 0

        while node:
            list_len += 1
            node = node.next

        return list_len

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_len = self._get_list_len(head)
        if list_len <= 1:
            return head
        if list_len % 2 == 1 and (list_len + 1) / 2 == k:
            return head


        node = dummy_head = ListNode(-1, head)
        cur_node_idx = 0

        before_k_node, k_node, before_last_k_node, last_k_node = None, None, None, None
        if k > list_len / 2:
            k = list_len - k + 1

        while node:
            if cur_node_idx == k - 1:
                before_k_node = node
            elif cur_node_idx == k:
                k_node = node
            elif cur_node_idx == list_len - k:
                before_last_k_node = node
            elif cur_node_idx == list_len + 1 - k:
                last_k_node = node
                break

            node = node.next
            cur_node_idx += 1

        before_k_node.next = last_k_node
        if last_k_node is k_node.next:
            last_k_node.next, k_node.next = k_node, last_k_node.next
        else:
            last_k_node.next, k_node.next = k_node.next, last_k_node.next
            before_last_k_node.next = k_node

        return dummy_head.next

    def swapNodes_946ms_sol(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        ek 노드를 찾는 우아한 투 포인터 아이디어
        """
        cur = head
        for _ in range(k - 1):
            cur = cur.next
        bk, ek = cur, head
        while cur.next:
            ek = ek.next
            cur = cur.next
        if ek is not bk:
            bk.val, ek.val = ek.val, bk.val
        return head
