"""
https://leetcode.com/problems/intersection-of-two-linked-lists/

> Topic: Hash Table (Set) / Linked List / Two Pointers (Double Pointer)
> Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?

Ref)
- https://dev.to/seanpgallivan/solution-intersection-of-two-linked-lists-478e
- https://dev.to/thivyaamohan/160-intersection-of-two-linked-lists-leetcode-3f3d
- https://github.com/azl397985856/leetcode/blob/master/problems/160.Intersection-of-Two-Linked-Lists.en.md

The naive approach here would be to store each node reference in a data structure until we saw the same one twice,
but that would take O(N) extra space.

In order to solve this problem with only O(1) extra space,
we'll need to find another way to align the two linked lists.
More importantly, we need to find a way to line up the ends of the two lists.
And the easiest way to do that is to concatenate them in opposite orders, A+B and B+A.
This way, the ends of the two original lists will align on the second half of each merged list.

Then we just need to check if at some point the two merged lists are pointing to the same node.
In fact, even if the two merged lists don't intersect,
the value of a and b will be the same (null) when we come to the end of the merged lists,
so we can use that as our exit condition.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Time Complexity: O(m + n)
        (Extra) Space Complexity: O(m)
        """
        visited = set()
        node_in_a, node_in_b = headA, headB

        while node_in_a:
            visited.add(node_in_a)
            node_in_a = node_in_a.next

        while node_in_b:
            if node_in_b in visited:
                return node_in_b

            node_in_b = node_in_b.next

    def getIntersectionNodeTwoPointer(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Time Complexity: O(m + n)
        (Extra) Space Complexity: O(1)

        concatenate them in opposite orders, A+B and B+A.
        This way, the ends of the two original lists will align on the second half of each merged list.
        """
        a, b = headA, headB
        while a is not b:
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
