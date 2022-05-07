"""
https://leetcode.com/problems/sort-array-by-parity/
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(n)
        """
        even_nums, odd_nums = [], []

        for n in nums:
            if n % 2:
                odd_nums.append(n)
            else:
                even_nums.append(n)

        return even_nums + odd_nums

    def sortArrayByParityWithArgSpaceTrick(self, nums: List[int]) -> List[int]:
        """
        > Arg Space Trick
        > Like Bubble Sort

        시간 복잡도: O(n)
        공간 복잡도: O(1)
        """
        if len(nums) == 1:
            return nums
        index = 0

        for i in range(len(nums)):
            print(f'nums[i:{i}]: {nums[i]}')
            if nums[i] % 2 != 0:
                continue
            nums[index], nums[i] = nums[i], nums[index]
            print('> index:', index, nums)
            index += 1

        return nums


if __name__ == '__main__':
    sol = Solution()
    # test_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # test_case = [1, 1, 1, 1, 1]
    # test_case = [2, 4, 6, 8, 10]
    test_case = [1, 2, 2, 2, 2, 2, 2]
    sol.sortArrayByParityWithArgSpaceTrick(test_case)
