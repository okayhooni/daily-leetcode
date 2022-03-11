"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

파이썬 알고리즘 인터뷰 서적 관련 문제)
p.220 : 역순 연결 리스트(node, prev)
p.231 : 페어의 노드 스왑(더미 헤드)
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        node, prev = head, dummy_head

        while node and node.next:
            if node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node.next = node.next.next

                prev.next = node = node.next
            else:
                prev = node
                node = node.next

        return dummy_head.next
