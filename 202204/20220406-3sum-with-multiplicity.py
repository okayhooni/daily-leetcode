from typing import List
from collections import Counter


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        distinct_arr = sorted(set(arr))
        counter = Counter(arr)
        res_cnt = 0

        # print(distinct_arr)
        # print(counter)
        for first_idx, first_num in enumerate(distinct_arr):
            if counter[first_num] >= 3 and first_num * 3 == target:
                tmp_cnt = counter[first_num] * (counter[first_num] - 1) * (counter[first_num] - 2) / 6
                # print(f'> {tmp_cnt}')
                res_cnt += tmp_cnt

            if counter[first_num] >= 2 and target - first_num * 2 != first_num and (target - first_num * 2) in counter:
                tmp_cnt = (counter[first_num] * (counter[first_num] - 1) / 2) * counter[target - first_num * 2]
                # print(f'>> {tmp_cnt}')
                res_cnt += tmp_cnt

            if first_idx < len(distinct_arr) - 2:
                second_idx = first_idx + 1
                third_idx = len(distinct_arr) - 1

                while second_idx < third_idx:
                    second_num, third_num = distinct_arr[second_idx], distinct_arr[third_idx]
                    cur_sum = first_num + second_num + third_num

                    if cur_sum < target:
                        second_idx += 1
                    elif cur_sum > target:
                        third_idx -= 1
                    else:
                        res_cnt += counter[first_num] * counter[second_num] * counter[third_num]
                        second_idx += 1
                        third_idx -= 1

        return int(res_cnt) % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    # print(sol.threeSumMulti([0, 0, 0], 0))
    print(sol.threeSumMulti([0 for _ in range(3000)], 0))
