"""
https://leetcode.com/problems/add-two-numbers
"""
from typing import Optional
from functools import reduce


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """
    def _add_two_with_upcoming(self, n1: ListNode, n2: ListNode = None, upcoming: int = 0) -> (ListNode, int):
        val = n1.val
        if n2:
            val += n2.val
        if upcoming:
            val += upcoming

        upcoming, res = divmod(val, 10)

        return ListNode(res), upcoming

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = l1, l2
        result = dummy_head = ListNode()
        upcoming = 0

        while first or second:
            if not first:
                result.next, upcoming = self._add_two_with_upcoming(second, upcoming=upcoming)
                second = second.next
            elif not second:
                result.next, upcoming = self._add_two_with_upcoming(first, upcoming=upcoming)
                first = first.next
            else:
                result.next, upcoming = self._add_two_with_upcoming(first, second, upcoming=upcoming)
                first, second = first.next, second.next

            result = result.next

        if upcoming:
            result.next = ListNode(upcoming)

        return dummy_head.next

    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """기억은 안나지만 아주 오래전에 풀었던 기록이 있는 코드 1"""
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            cur_sum = getattr(l1, 'val', 0) + getattr(l2, 'val', 0) + carry
            carry, cur_val = divmod(cur_sum, 10)
            head.val = cur_val

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if not l1 and not l2 and not carry:
                break

            head.next = ListNode()
            head = head.next

        return root

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """기억은 안나지만 아주 오래전에 풀었던 기록이 있는 코드 2"""
        def adder(x, y, over_val=0):
            x_val = x.val if x else 0
            y_val = y.val if y else 0
            x_next = x.next if x else None
            y_next = y.next if y else None
            over, r_val = divmod(x_val + y_val + over_val, 10)

            if not over and not x_next and not y_next and x_val + y_val + over_val == 0:
                return None

            next_node = adder(x_next, y_next, over)
            return ListNode(r_val, next_node)

        res = adder(l1, l2)
        return res if res else ListNode(0)

    def addTwoNumbers3(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """기억은 안나지만 아주 오래전에 풀었던 기록이 있는 코드 3"""
        i1 = self.list_node_to_int(l1)
        i2 = self.list_node_to_int(l2)
        s = i1 + i2
        return self.int_to_list_node(s)

    def list_node_to_int(self, list_node):
        p_list = []
        while list_node:
            p_list.append(list_node.val)
            list_node = list_node.next
        p_list.reverse()
        return reduce(lambda x, y: 10 * x + y, p_list)

    def int_to_list_node(self, integer):
        root = head = ListNode(0)
        s = str(integer)
        l = len(s)
        for k, i in enumerate(reversed(s)):
            head.val = i
            if k >= l - 1:
                break

            head.next = ListNode()
            head = head.next

        return root
