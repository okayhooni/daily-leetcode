"""
https://leetcode.com/problems/furthest-building-you-can-reach/

> Topic: Heap (Priority Queue) / Greedy Algorithm

Hint 1) Assume the problem is to check whether you can reach the last building or not.
Hint 2) You'll have to do a set of jumps, and choose for each one whether to do it using a ladder or bricks.
It's always optimal to use ladders in the largest jumps.
Hint 3) Iterate on the buildings, maintaining the largest r jumps and the sum of the remaining ones so far,
and stop whenever this sum exceeds b.

Ref) https://dev.to/seanpgallivan/solution-furthest-building-you-can-reach-1m24

The first realization should be that we always want to use our ladders to their best effect:
where they would save us the most amount of bricks.
Unfortunately, we can't just save the ladders for the largest gaps in the building heights,
because we may not be able to reach them by using bricks.

Since we can't find out how far we can go until we figure out where to place the ladders,
and we can't figure out where to put the ladders until we see how far we can go,
we'll have to move the ladders around as we go in order to maintain their maximum effect.

To put this in terms of a coding solution, as we iterate through the building heights array (H),
we'll want to continuously make sure that the largest L number of positive differences are occupied with ladders,
allowing us the best use of our B number of bricks.

In general, this means that we should start iterating through H, ignoring any difference (diff) that is 0 or less,
and place a ladder whenever we have a positive difference.
Once we've used up all the ladders, then we can start using bricks.
If we come across a diff that is larger than the smallest ladder that we're currently using,
we should replace that ladder with bricks and move the ladder forward to the current diff.
Otherwise, we should use bricks for the current diff.

The second big realization at this point is that we need a min-heap or min priority queue,
in order to keep track of the heights of the ladders in use,
so that we can always take the smallest one, thus keeping the ladders always on the largest diff values.

If at any point we run out bricks, then we can't reach the next building and should return i.
If we're able to reach the end of H without running out of bricks, we can return H.length - 1,
signifying that we reached the last building.
"""
from typing import List
from heapq import heappush, heapreplace  # , heappop


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Time Complexity: O(N) where N is the length of H - all the heights on the input can be popped at most once!
        Space Complexity: O(L) to keep track of L number of ladder lengths
        """
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue

            if ladders > 0:
                heappush(heap, diff)
                ladders -= 1
            elif heap and diff > heap[0]:
                # bricks -= heappop(heap)
                # heappush(heap, diff)
                bricks -= heapreplace(heap, diff)
            else:
                bricks -= diff

            if bricks < 0:
                return i

        return len(heights) - 1
