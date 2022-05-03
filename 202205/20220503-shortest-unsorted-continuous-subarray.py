"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

> Follow up: Can you solve it in O(n) time complexity?
"""
from typing import List


class Solution:
    def findUnsortedSubarrayWithSort(self, nums: List[int]) -> int:
        """
        시간 복잡도: O(n * log(n))
        공간 복잡도: O(n)
        """
        sorted_nums = sorted(nums)

        for idx, (n, s) in enumerate(zip(nums, sorted_nums)):
            if n != s:
                subarray_start_idx = idx
                break
        else:
            return 0

        for rev_idx, (n, s) in enumerate(zip(reversed(nums), reversed(sorted_nums))):
            if n != s:
                subarray_end_idx = len(nums) - rev_idx - 1
                break
        else:
            return 0

        return subarray_end_idx - subarray_start_idx + 1

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        > Follow up: Can you solve it in O(n) time complexity?

        시간 복잡도: O(n)
        공간 복잡도: O(1)
        """
        len_nums = len(nums)
        if len_nums <= 1:
            return 0

        left_idx, right_idx = 0, len_nums - 1

        while left_idx < len_nums - 1 and nums[left_idx] <= nums[left_idx + 1]:
            left_idx += 1

        if left_idx == len_nums - 1:
            return 0

        while 0 < right_idx and nums[right_idx - 1] <= nums[right_idx]:
            right_idx -= 1

        # if left_idx > right_idx:
        #     return 0

        # sub_arrays = nums[left_idx:right_idx + 1]
        # sub_min, sub_max = min(sub_arrays), max(sub_arrays)
        sub_min = sub_max = nums[left_idx]
        sub_idx = left_idx + 1
        while sub_idx <= right_idx:  # for O(1) space complexity with no copy operation on list slicing
            sub_min = min(sub_min, nums[sub_idx])
            sub_max = max(sub_max, nums[sub_idx])
            sub_idx += 1

        while 0 < left_idx and nums[left_idx - 1] > sub_min:
            left_idx -= 1

        while right_idx < len(nums) - 1 and sub_max > nums[right_idx + 1]:
            right_idx += 1

        return right_idx - left_idx + 1

    def findUnsortedSubarrayWrong(self, nums: List[int]) -> int:
        """
        CANNOT HANDLE SOME CASES LIKE [1, 3, 2, 2, 2]
        """
        len_nums = len(nums)
        if len_nums <= 1:
            return 0

        idx = 1
        while idx < len_nums:
            if nums[idx - 1] > nums[idx]:
                subarray_start_idx = idx - 1
                break

            idx += 1
        else:
            return 0

        jdx = len_nums - 1
        while 0 < jdx:
            if nums[jdx - 1] > nums[jdx]:
                subarray_end_idx = jdx
                break

            jdx -= 1
        else:
            return 0

        return subarray_end_idx - subarray_start_idx + 1

    def findUnsortedSubarrayWrong2(self, nums: List[int]) -> int:
        """
        CANNOT HANDLE SOME CASES LIKE [1, 2, 4, 5, 3]
        """
        len_nums = len(nums)
        if len_nums <= 1:
            return 0

        idx = 1
        subarray_start_idx, subarray_end_idx = None, None
        max_val_on_array = nums[0]
        start_idx_of_cur_num = 0
        while idx < len_nums:
            if subarray_start_idx is None and nums[idx - 1] > nums[idx]:
                subarray_start_idx = min(start_idx_of_cur_num, idx - 1)

            if nums[idx - 1] != nums[idx]:
                start_idx_of_cur_num = idx

            max_val_on_array = max(max_val_on_array, nums[idx])

            if max_val_on_array > nums[idx]:
                subarray_end_idx = idx

            idx += 1

        if subarray_start_idx is not None:
            return subarray_end_idx - subarray_start_idx + 1
        else:
            return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.findUnsortedSubarray([1, 2, 3, 4, 5]))
    # print(sol.findUnsortedSubarray([1, 3, 2, 2, 2]))
    # print(sol.findUnsortedSubarray([2, 3, 3, 2, 4]))
    print(sol.findUnsortedSubarray([1, 2, 4, 5, 3]))
