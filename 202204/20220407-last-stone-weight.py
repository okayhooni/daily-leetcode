"""
https://leetcode.com/problems/last-stone-weight/
"""
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    """
    시간 복잡도: O(n) + O(n * log(n)) = O(n * log(n))
    공간 복잡도: O(n)
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones = [-s for s in stones]
        heapify(negative_stones)

        while negative_stones:
            cur_first_stone = -heappop(negative_stones)

            try:
                cur_second_stone = -heappop(negative_stones)
            except IndexError:
                return cur_first_stone

            if cur_first_stone != cur_second_stone:
                heappush(negative_stones, cur_second_stone - cur_first_stone)

        return 0
