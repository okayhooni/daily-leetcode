"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:
    key_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        cur_char_list = list(self.key_map[digits[0]])

        total_len = len(digits)
        if total_len == 1:
            return cur_char_list

        suffix_str = digits[1:]
        suffix_list = self.letterCombinations(suffix_str)

        return [
            f'{cur_char}{suffix_chars}'
            for cur_char in cur_char_list
            for suffix_chars in suffix_list
        ]

    def letterCombinationsWithDFS(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for j in self.key_map[digits[index]]:
                dfs(index + 1, path + j)

        if not digits:
            return []

        result = []
        dfs(0, "")
        # print('cnt:', cnt)  # cnt: 13 / cnt: 40
        return result


if __name__ == '__main__':
    print(Solution().letterCombinations("234"))
    print(Solution().letterCombinationsWithDFS("234"))
