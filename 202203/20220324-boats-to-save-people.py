"""
https://leetcode.com/problems/boats-to-save-people
"""
from typing import List
from collections import deque


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        시간 복잡도: O(n*log(n))
        공간 복잡도: O(n)
        """
        sorted_people = deque(sorted(people))

        res_cnt = 0

        while sorted_people:
            most_heavy_man_remained = sorted_people.pop()

            if sorted_people and sorted_people[0] + most_heavy_man_remained <= limit:
                sorted_people.popleft()

            res_cnt += 1

        return res_cnt

    def numRescueBoats_416ms_sample(self, people: List[int], limit: int) -> int:
        """
        투-포인터 방식, in-place 소팅으로 공간복잡도 줄였지만, 외부에서 전달된 인자를 수정한다는 단점

        시간 복잡도: O(n*log(n))
        공간 복잡도: O(1)
        """
        people.sort()
        left, right, res = 0, len(people) - 1, 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            res += 1
            right -= 1
        return res
