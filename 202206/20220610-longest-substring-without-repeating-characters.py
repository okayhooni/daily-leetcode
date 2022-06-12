"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

> Topic: Two Pointers (Double Pointer) / Sliding Window / Hash Table (Set/Dict)
"""
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_char_to_idx_map = {}
        cur_str_chars = deque()
        longest_substr_len = cur_str_len = 0

        for cur_idx, cur_char in enumerate(s):
            if cur_str_len + len(s) - cur_idx < longest_substr_len:
                break

            if cur_char in seen_char_to_idx_map:
                cur_str_len = cur_idx - seen_char_to_idx_map[cur_char]

                while cur_str_chars[0] != cur_char:
                    seen_char_to_idx_map.pop(cur_str_chars.popleft())
                cur_str_chars.popleft()
            else:
                cur_str_len += 1
                longest_substr_len = max(longest_substr_len, cur_str_len)

            # print(cur_str_len, seen_char_to_idx_map)
            seen_char_to_idx_map[cur_char] = cur_idx
            cur_str_chars.append(cur_char)

        return longest_substr_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        used = {}
        cur_start_idx = 0
        max_len = 0

        for idx, char in enumerate(s):
            if (idx - cur_start_idx + 1) + (len(s) - idx) < max_len:
                break

            prev_idx = used.get(char)
            if prev_idx is not None and cur_start_idx <= prev_idx:
                cur_start_idx = prev_idx + 1
            else:
                # cur_len = idx - cur_start_idx + 1
                max_len = max(max_len, idx - cur_start_idx + 1)

            used[char] = idx

        return max_len


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('tmmzuxt'))
    print(sol.lengthOfLongestSubstring2('tmmzuxt'))
