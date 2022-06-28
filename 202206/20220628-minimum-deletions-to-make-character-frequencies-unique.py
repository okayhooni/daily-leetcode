"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

> Topic: Math / Greedy Algorithm / Sorting

Hint)
- As we can only delete characters,
  if we have multiple characters having the same frequency, we must decrease all the frequencies of them, except one.
- Sort the alphabet characters by their frequencies non-increasingly.
- Iterate on the alphabet characters, keep decreasing the frequency of the current character
  until it reaches a value that has not appeared before.
"""
from collections import Counter, defaultdict


class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Time Complexity: O(N)
        Auxiliary Space Complexity: O(N)
        """
        char_counter = Counter(s)

        char_nums_by_cnt = defaultdict(int)
        for char, cnt in char_counter.items():
            char_nums_by_cnt[cnt] += 1

        deletion_cnt = 0

        max_cnt = max(char_nums_by_cnt)
        for cnt in range(max_cnt, 0, -1):
            if char_nums_by_cnt[cnt] > 1:
                deletion_cnt += char_nums_by_cnt[cnt] - 1
                char_nums_by_cnt[cnt - 1] += char_nums_by_cnt[cnt] - 1

        return deletion_cnt


if __name__ == '__main__':
    sol = Solution()
    assert sol.minDeletions("aab") == 0
    assert sol.minDeletions("aaabbbcc") == 2
    assert sol.minDeletions("ceabaacb") == 2
