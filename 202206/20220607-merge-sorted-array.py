"""
https://leetcode.com/problems/merge-sorted-array/

> Topic: Two Pointers (Double Pointer) / Backward Pointers [= Reverse Pointers] / Sorting
> Follow up: Can you come up with an algorithm that runs in O(m + n) time?

Hint 1) You can easily solve this problem if you simply think about two elements at a time rather than two arrays.
We know that each of the individual arrays is sorted. What we don't know is how they will intertwine.
Can we take a local decision and arrive at an optimal solution?

Hint 2) If you simply consider one element each at a time from the two arrays,
and make a decision and proceed accordingly, you will arrive at the optimal solution.

"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Time Complexity: O(2 * m + n) = O(m + n)
        (Extra) Space Complexity: O(m)
        """
        nums1_tmp = nums1[:m]
        idx_1 = idx_2 = 0
        while idx_1 < m or idx_2 < n:
            if idx_2 == n or (idx_1 < m and nums1_tmp[idx_1] <= nums2[idx_2]):
                nums1[idx_1 + idx_2] = nums1_tmp[idx_1]
                idx_1 += 1
            else:
                nums1[idx_1 + idx_2] = nums2[idx_2]
                idx_2 += 1

    def mergeWithArgSpaceTrick(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        > Backward Pointers [= Reverse Pointers]

        Time Complexity: O(m + n)
        (Extra) Space Complexity: O(1)
        """
        while 0 < m and 0 < n:

            if nums1[m - 1] <= nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1

        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1


if __name__ == '__main__':
    sol = Solution()
    test_input = [1, 2, 3, 0, 0, 0]
    # sol.merge(test_input, 3, [2, 5, 6], 3)
    sol.mergeWithArgSpaceTrick(test_input, 3, [2, 5, 6], 3)
    print(test_input)
