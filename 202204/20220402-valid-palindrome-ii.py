"""
https://leetcode.com/problems/valid-palindrome-ii
"""


class Solution:
    """
    모든 풀이 공통

    시간 복잡도: O(n)
    공간 복잡도: O(1) ~ O(n) : 리스트 슬라이싱
    """
    def _is_valid_palindrom(self, s: str, has_one_more_chance: bool) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                if not has_one_more_chance:
                    return False

                return self._is_valid_palindrom(s[left:right], has_one_more_chance=False) or \
                    self._is_valid_palindrom(s[left+1:right+1], has_one_more_chance=False)

            left += 1
            right -= 1

        return True

    def validPalindromeWithRecursion(self, s: str) -> bool:
        return self._is_valid_palindrom(s, has_one_more_chance=True)

    def validPalindrome(self, s: str) -> bool:
        def _is_palindrome(sub_str: str) -> bool:
            return sub_str == sub_str[::-1]

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return _is_palindrome(s[left:right]) or _is_palindrome(s[left + 1:right + 1])

            left += 1
            right -= 1

        return True

    def validPalindrome_44ms_sol(self, s: str) -> bool:
        """
        투 포인터 체크 이동 간격 x > 1로 가속
        """
        is_pal = lambda s: s == s[::-1]

        left = 0
        right = len(s) - 1
        x = len(s) // 2

        while right > left:
            if s[left:left + x] == s[right:right - x:-1]:
                left = left + x
                right = right - x
            elif x > 1:
                x //= 2
            else:
                return is_pal(s[left:right]) or is_pal(s[left + 1:right + 1])

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.validPalindrome(
        "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxj"
        "jxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    ))
