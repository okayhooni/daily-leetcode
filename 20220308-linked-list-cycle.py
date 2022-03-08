"""
https://leetcode.com/problems/linked-list-cycle

파이썬 알고리즘 인터뷰 서적 관련 문제)
p.210 : 러너 기법(팰린드롬 연결 리스트)
p.364 : 코스 스케줄(순환 그래프 판별)
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    """
    # 1. 해시 테이블 기반 집합 set 이용 풀이
    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited = set()
        node = head

        while node is not None:
            if node in visited:
                return True

            # 해시 가능함(hashable)의 정의: from Fluent Python(p. 111)
            # 수명 주기동안 결코 변하지 않는 해시값을 갖고 있고(__hash__()),
            # 다른 객체와 비교할 수 있으면(__eq__()), 객체를 해시 가능하다고 한다.
            # 동일하다고 판단되는 객체는 반드시 해시값이 동일해야 한다.
            visited.add(node)
            # 사용자 정의 자료형은 기본적으로 해시 가능
            # 기본적으로 객체의 해시값은 id()를 이용해서 구하므로 모든 객체가 서로 다르기 떄문
            # CPython의 경우 id()는 객체의 메모리 주소를 반환 from Fluent Python(p. 295)
            node = node.next

        return False


# Follow up: Can you solve it using O(1) (i.e. constant) memory?
class Solution2:
    """
    # 2. 투 포인터(러너 기법) 이용 풀이
    시간 복잡도: O(n)
    공간 복잡도: O(1)

    cycle 이 존재한다면, fast 포인터가 무한히 순환하므로 언젠가 slow 포인터와 만나게 된다.
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow, fast = head, head.next

        while fast and fast.next:
            if slow is fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
