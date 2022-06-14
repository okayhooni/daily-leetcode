"""
https://leetcode.com/problems/delete-operation-for-two-strings/

> Topic: Dynamic Programming

Ref) https://dev.to/seanpgallivan/solution-delete-operation-for-two-strings-235k

longest common subsequence (LCS) between the two words (W1, W2).
The answer will then be the combined difference between the length of the words and the length of the LCS.

For a typical LCS solution, we would use a bottom-up dynamic programming (DP) approach,
and use nested loops to compare each letter of each word against each other (W1[i], W2[j]).
This would normally call for a DP array of size (m + 1) * (n + 1), where m = W1.length and n = W2.length.

Since the DP array is being built iteratively, in order,
we can reduce the normal space complexity from O(N * M) by only keeping the current and last rows (dpCurr, dpLast)
as we iterate through.
This will drop the space complexity to O(N).
Doing this, we can also ensure that the shorter word is used for N by swapping the two words if necessary.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time Complexity: O(N * M) where N and M are the lengths of the two words
        (Extra) Space Complexity: O(N * M)
        """
        dp = [[0 for _ in range(len(word2) + 1)]]

        for i1, c1 in enumerate(word1, 1):
            dp.append([0])
            for i2, c2 in enumerate(word2, 1):
                # print(i1, i2, '/', dp)
                if c1 == c2:
                    cur = dp[i1 - 1][i2 - 1] + 1
                else:
                    cur = max(dp[i1][i2 - 1], dp[i1 - 1][i2])

                dp[-1].append(cur)

        return len(word1) + len(word2) - 2 * dp[-1][-1]

    def minDistanceMoreCompact(self, word1: str, word2: str) -> int:
        """
        Time Complexity: O(N * M) where N and M are the lengths of the two words
        (Extra) Space Complexity: O(N) where N is the length of the smaller of the two words
        """
        if len(word1) >= len(word2):
            long_word, short_word = word1, word2
        else:
            long_word, short_word = word2, word1

        dp_prev = [0 for _ in range(len(short_word) + 1)]
        dp_cur = dp_prev[:]

        for i1, c1 in enumerate(long_word, 1):
            for i2, c2 in enumerate(short_word, 1):
                if c1 == c2:
                    dp_cur[i2] = dp_prev[i2 - 1] + 1
                else:
                    dp_cur[i2] = max(dp_cur[i2 - 1], dp_prev[i2])

            # print(dp_cur)
            dp_cur, dp_prev = dp_prev, dp_cur

        return len(word1) + len(word2) - 2 * dp_prev[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance("sea", "eat"))
    print(sol.minDistanceMoreCompact("sea", "eat"))
