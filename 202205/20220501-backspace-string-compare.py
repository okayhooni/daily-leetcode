"""
https://leetcode.com/problems/backspace-string-compare/
"""


class Solution:
    @staticmethod
    def convert_string_with_stack(input_str: str) -> str:
        stack = []
        for char in input_str:
            if char == '#':
                try:
                    stack.pop()
                except IndexError:
                    pass
            else:
                stack.append(char)

        return ''.join(stack)

    def backspaceCompareWithStack(self, s: str, t: str) -> bool:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(n)
        """
        return self.convert_string_with_stack(s) == self.convert_string_with_stack(t)

    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Follow up: Can you solve it in O(n) time and O(1) space?

        Backward Pointers

        시간 복잡도: O(n)
        공간 복잡도: O(1)
        """
        s_idx, t_idx = len(s) - 1, len(t) - 1
        s_skip_char_nums, t_skip_char_nums = 0, 0

        while 0 <= s_idx or 0 <= t_idx:
            # print(f'[s_idx: {s_idx}][t_idx: {t_idx}]')

            while 0 <= s_idx:
                if s[s_idx] == '#':
                    s_skip_char_nums += 1
                    s_idx -= 1
                elif s_skip_char_nums:
                    # s_idx -= s_skip_char_nums
                    s_skip_char_nums -= 1
                    s_idx -= 1
                else:
                    break

            while 0 <= t_idx:
                if t[t_idx] == '#':
                    t_skip_char_nums += 1
                    t_idx -= 1
                elif t_skip_char_nums:
                    # t_idx -= t_skip_char_nums
                    t_skip_char_nums -= 1
                    t_idx -= 1
                else:
                    break

            # print(f's_idx: {s_idx} / s[s_idx]: {s[s_idx]} | t_idx: {t_idx} / s[t_idx]: {t[t_idx]}')
            if 0 <= s_idx and 0 <= t_idx and s[s_idx] != t[t_idx]:
                return False
            if (0 <= s_idx) ^ (0 <= t_idx):
                return False

            s_idx -= 1
            t_idx -= 1

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.backspaceCompare("ab##", "c#d#"))
    print(sol.backspaceCompare("a##c", "#a#c"))
    print(sol.backspaceCompare("bxj##tw", "bxj###tw"))
    print(sol.backspaceCompare("bxj##tw", "bxo#j##tw"))
