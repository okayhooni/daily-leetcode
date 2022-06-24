"""
https://leetcode.com/problems/construct-target-array-with-multiple-sums/

> Topic: Heap (Priority Queue)

Hint 1) Given that the sum is strictly increasing,
the largest element in the target must be formed in the last step by adding the total sum in the previous step.
Thus, we can simulate the process in a reversed way.

Hint 2) Subtract the largest with the rest of the array, and put the new element into the array.
Repeat until all elements become one

Ref) https://dev.to/seanpgallivan/solution-construct-target-array-with-multiple-sums-24d4

One thing we can notice right away:
The sum of the elements in A will always be larger than any single element of A,
since A starts off with all positive numbers.
Therefore, the sum will only ever go up as we iterate through the solution process.
This means that we will only ever have one attempt to place a given number in its correct spot.

It also means that the last step will always be to settle the highest value of the target array,
which means we can reconstruct the nature of A right before the last step as well.

From there, we'll have to keep dealing with the largest remaining value, on and on,
working backwards until we either succeed or fail.

Since we are going to have to deal with the target values in descending value order,
it stands to reason that we should use a max priority queue or max-heap structure to keep track of the target values,
especially since we don't care about the values' indices.

Once we have all the target values inserted into the priority queue (pq/heap) and the sum calculated,
we can proceed to deal with the values in order.

At each step, we should remove the max value, compute its replacement's value,
then reinsert that replacement back into pq.

If, at the start of an iteration, we see that the max value in pq is a 1,
then that means that all values in pq are 1s, and we should return true.

On the other hand, if we find ourselves about to insert a number less than 1 into pq,
we know we've failed and should return false, as we will have passed the prescribed starting position.
"""
from typing import List
from heapq import heapify, heappop, heappush
"""
[a + b + c = d]

a + b + d = s
a + b + c = d ~> c = d - (a + b)

d - c = s - d
c = 2 * d - s

new_s = s - d + c
"""


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        cur_sum = sum(target)
        if len(target) == 1 and cur_sum != 1:
            return False

        negative_heap = [-num for num in target]
        heapify(negative_heap)

        while negative_heap[0] < -1:
            # print(negative_heap)
            cur_max_element = -heappop(negative_heap)
            previous_element = 2 * cur_max_element - cur_sum
            previous_element = cur_sum % (cur_sum - previous_element)
            # print(previous_element)
            if previous_element < 1:  # ~= previous_element <= 0 : [if num <= total]
                return False
            if cur_sum == previous_element:  # [total < 1 ~ total <= 0]
                return False
            """
            But at this point, we'll still obtain a TLE result and will need to optimize some more.
            Consider the situation in which we process the max value only to find that we're about to reinsert a number,
            that is still the max value.
            In some edge cases, it could take thousands of iterations to fully process this value
            so that we can move on to another, when all that processing can be done more simply in one step.

            Take, for example, target = [3,5,33]. Normally, we'd remove the 33 and compute its replacement to be 25,
            then from 25 to 17, then 17 to 9, then finally 9 to 1.
            Each time, we're removing the sum of all the remaining values (3 + 5 = 8) from the current number.
            In any valid target array, as we noted at the very beginning,
            the max value must be larger than the sum of the remaining elements,
            since it came from that sum plus the value that was replaced.

            That means that we should be able to remove the remaining sum (8) from our current max value (33)
            as many times as we possibly can, since only the remainder will bring us below that sum.
            This we can achieve quite easily with the mod operator,
            which will result in our replacement value (33 % 8 = 1) without the need to iterate through every step.

            As noted recently, if we find that the max value is actually less than the remaining sum,
            then the array must not be valid, and we can return false.
            
            Also, if num should end up being 0 after applying the mod operator,
            then we should return false, except for the edge case where sum = 1.
            
            Alternately, we could instead push sum onto pq intead of num,
            which will immediately trigger a failure in all but the edge case.
            """
            heappush(negative_heap, -previous_element)
            cur_sum = cur_sum - cur_max_element + previous_element
            # print(negative_heap)

        return negative_heap[0] == -1

    def isPossibleRef(self, target: List[int]) -> bool:
        heap = [-num for num in target]
        total = sum(target)
        heapify(heap)
        while heap[0] != -1:
            num = -heappop(heap)
            total -= num
            if num <= total or total < 1:
                return False
            # print(num, total, num % total)
            num %= total
            total += num
            # print(num, total)
            heappush(heap, -num or -total)
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPossible([9, 3, 5])
    assert not sol.isPossible([1, 1, 1, 2])
    assert sol.isPossible([1, 1000000000])
    assert sol.isPossible([2, 900000001])
    assert not sol.isPossible([2, 900000002])
    assert not sol.isPossible([1, 1, 10])
    assert not sol.isPossible([2])
    assert not sol.isPossibleRef([1, 1, 10])
