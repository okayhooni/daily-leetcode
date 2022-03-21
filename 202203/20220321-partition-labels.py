"""
https://leetcode.com/problems/partition-labels
"""
from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        idx_list_by_char = defaultdict(list)

        for idx, char in enumerate(s):
            idx_list_by_char[char].append(idx)

        chunks = [[0, 0]]
        idx, total_len = 0, len(s)

        while idx < total_len:
            last_idx_of_cur_char = idx_list_by_char[s[idx]][-1]

            if idx > chunks[-1][-1]:
                chunks.append([idx, last_idx_of_cur_char])
            else:
                chunks[-1][-1] = max(chunks[-1][-1], last_idx_of_cur_char)

            idx += 1

        return [last_idx - start_idx + 1 for start_idx, last_idx in chunks]


if __name__ == '__main__':
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))
