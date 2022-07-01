"""
https://leetcode.com/problems/maximum-units-on-a-truck/

> Topic: Math / Greedy Algorithm / Sorting

Hint)
- If we have space for at least one box, it's always optimal to put the box with the most units.
- Sort the box types with the number of units per box non-increasingly.
- Iterate on the box types and take from each type as many as you can.

Ref) https://dev.to/seanpgallivan/solution-maximum-units-on-a-truck-ak2
"""
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda b: b[1], reverse=True)
        ans_units = 0
        for box_num, unit_per_box in boxTypes:
            if truckSize < box_num:
                ans_units += unit_per_box * truckSize
                break

            ans_units += unit_per_box * box_num
            truckSize -= box_num

        return ans_units


if __name__ == "__main__":
    sol = Solution()
    assert sol.maximumUnits([[1, 3], [2, 2], [3, 1]], 4) == 8
