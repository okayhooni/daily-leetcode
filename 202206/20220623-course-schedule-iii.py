"""
https://leetcode.com/problems/course-schedule-iii/

cf) https://leetcode.com/problems/furthest-building-you-can-reach/

> Topic: Heap (Priority Queue) / Greedy Algorithm

Hint) During iteration, say I want to add the current course,
currentTotalTime being total time of all courses taken till now,
but adding the current course might exceed my deadline or it doesn’t.

1. If it doesn’t, then I have added one new course.
Increment the currentTotalTime with duration of current course.

2. If it exceeds deadline, I can swap current course with current courses that has biggest duration.
* No harm done and I might have just reduced the currentTotalTime, right?
* What preprocessing do I need to do on my course processing order so that this swap is always legal?

Ref) https://dev.to/seanpgallivan/solution-course-schedule-iii-48hn
"""
from typing import List
from heapq import heappush, heapreplace


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        Time Complexity: O(N * log N) where N is the length of C,
                         due to both the sort and the priority queue / heap implementation
        Space Complexity: O(N) due to the priority queue / heap data
        """
        courses.sort(key=lambda e: (e[1], e[0]))
        # courses.sort(key=lambda e: e[1]) : POSSIBLE
        total_day = 0
        crs_duration_heap = []

        for duration, last_day in courses:
            if total_day + duration <= last_day:
                total_day += duration
                heappush(crs_duration_heap, -duration)
            elif crs_duration_heap and -crs_duration_heap[0] > duration:
                total_day += duration + heapreplace(crs_duration_heap, -duration)

        return len(crs_duration_heap)


if __name__ == '__main__':
    sol = Solution()
    print(sol.scheduleCourse([[5, 5], [4, 6], [2, 6]]))
