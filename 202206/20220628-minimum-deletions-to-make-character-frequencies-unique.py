"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

> Topic: Math / Greedy Algorithm / Sorting ~ (Actually, sorting is not needed on this problem)

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
        Auxiliary Space Complexity: O(N) ~ char_nums_by_cnt
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

    def minDeletions2(self, s: str) -> int:
        """
        Time Complexity: O(N)
        Auxiliary Space Complexity: O(1) ~ O(26)
        """
        char_counter = Counter(s)
        seen_freq = set()
        deletion_cnt = 0

        for cnt in char_counter.values():
            while cnt > 0 and cnt in seen_freq:
                cnt -= 1
                deletion_cnt += 1

            seen_freq.add(cnt)

        return deletion_cnt

    def minDeletions103msSol(self, s: str) -> int:
        # calculate frequencies
        freq = [0] * 26
        for i in range(26):
            freq[i] = s.count(chr(ord('a') + i))
        delete_count = 0
        seen_frequencies = set()

        print(freq)
        for i in range(26):
            print(chr(ord('a') + i), freq[i])
            if freq[i] in seen_frequencies:
                while freq[i] > 0 and freq[i] in seen_frequencies:
                    delete_count += 1
                    freq[i] -= 1
            print('->', freq[i])
            seen_frequencies.add(freq[i])

        return delete_count


if __name__ == '__main__':
    sol = Solution()
    assert sol.minDeletions("aab") == 0
    assert sol.minDeletions("aaabbbcc") == 2
    assert sol.minDeletions("ceabaacb") == 2
    assert sol.minDeletions103msSol("ceabaacb") == 2
    assert sol.minDeletions103msSol("cadbddcb") == 2
