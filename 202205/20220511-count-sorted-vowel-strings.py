"""
https://leetcode.com/problems/count-sorted-vowel-strings/

- For each character, its possible values will depend on the value of its previous character,
  because it needs to be not smaller than it.

- Think backtracking.
  Build a recursive function count(n, last_character) that counts the number of valid strings of length n,
  and whose first characters are not less than last_character.

- In this recursive function,
  iterate on the possible characters for the first character,
  which will be all the vowels not less than last_character,
  and for each possible value c, increase the answer by count(n-1, c).
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
        Combination (n+4, 4)

        n + 5 개 칸 사이의 n + 4 개 칸막이 중에 4개 칸막이 위치 선택 경우의 수
        """
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24

    def countVowelStringsBruteForceDFS(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0

        def dfs(start_vowel_idx, remain_n):
            nonlocal count

            if remain_n == 0:
                count += 1
                return

            for vowel_idx in range(start_vowel_idx, len(vowels)):
                dfs(start_vowel_idx=vowel_idx, remain_n=remain_n - 1)

        dfs(start_vowel_idx=0, remain_n=n)

        return count

    def countVowelStringsMemoizeDP(self, n: int) -> int:
        DP_MAP = {
            (vowel_idx, 1): 5 - vowel_idx
            for vowel_idx in range(5)
        }

        def dfs(start_vowel_idx, remain_n):

            if (start_vowel_idx, remain_n) in DP_MAP:
                return DP_MAP[start_vowel_idx, remain_n]

            res = sum(
                dfs(start_vowel_idx=vowel_idx, remain_n=remain_n - 1)
                for vowel_idx in range(start_vowel_idx, 5)
            )

            DP_MAP[start_vowel_idx, remain_n] = res

            return res

        return dfs(start_vowel_idx=0, remain_n=n)

    def countVowelStringsTabulationDP(self, n: int) -> int:
        dp = [[5, 4, 3, 2, 1]]
        if n == 1:
            return 5
        for i in range(2, n):
            temp = []
            for j in range(5):
                temp.append(sum(dp[-1][j:]))
            dp.append(temp)
        # print(dp)
        return sum(dp[-1])

    def countVowelStringsTabulationDP2(self, n: int) -> int:
        # vows = ["a", "e", "i", "o", "u"]
        dp = [[]]
        dp[0] = [5, 4, 3, 2, 1]
        for i in range(1, n):
            dp.append([0] * 5)
            dp[i][4] = 1
            for j in range(3, -1, -1):
                dp[i][j] = dp[i][j + 1] + dp[i - 1][j]
        return dp[n - 1][0]

    def countVowelStringsWithoutDP(self, n: int) -> int:
        def dfs(start_vowel_idx, remain_n):
            if remain_n == 1:
                return 5 - start_vowel_idx

            res = sum(
                dfs(start_vowel_idx=vowel_idx, remain_n=remain_n - 1)
                for vowel_idx in range(start_vowel_idx, 5)
            )

            return res

        return dfs(start_vowel_idx=0, remain_n=n)
