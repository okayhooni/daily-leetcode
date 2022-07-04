"""
https://leetcode.com/problems/candy/

> Topic: Math / Greedy Algorithm

Ref) https://leetcode.com/problems/candy/solution/
"""
from typing import *


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Time complexity: O(n) ~ The array candies of size n is traversed thrice.
        Space complexity: O(n) ~ An array candies of size n is used.
        """
        candies = [1 for _ in ratings]
        prev_rate = None
        for idx, rate in enumerate(ratings):
            if idx != 0 and prev_rate < rate:
                candies[idx] = candies[idx - 1] + 1

            prev_rate = rate

        next_rate = None
        for jdx, rate in enumerate(reversed(ratings)):
            idx = len(ratings) - jdx - 1

            if idx != len(ratings) - 1 and rate > next_rate:
                candies[idx] = max(candies[idx], candies[idx + 1] + 1)

            next_rate = rate

        return sum(candies)


if __name__ == '__main__':
    sol = Solution()
    assert sol.candy([1, 0, 2]) == 5
    assert sol.candy([1, 2, 2]) == 4
    assert sol.candy([1, 3, 2, 2, 1]) == 7
    assert sol.candy([1, 3, 4, 5, 2]) == 11
