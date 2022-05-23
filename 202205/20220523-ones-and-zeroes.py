"""
https://leetcode.com/problems/ones-and-zeroes/

> Topic: Dynamic Programming

Ref)
- https://github.com/azl397985856/leetcode/blob/master/problems/474.ones-and-zeros-en.md
- https://dev.to/seanpgallivan/solution-ones-and-zeroes-2emf

> When see the requirement of returning maximum number, length etc, and not require to list all possible value.
Usually it can be solved by DP.

This problem we can see is a 0-1 backpack issue, either take current string or not take current string.

And during interview, DP problem is hard to come up with immediately,
recommend starting from Brute force, then optimize the solution step by step, until interviewer is happy, :-)

> In 3D DP solution, we kept track all state value, but we only need previous state,
so we can reduce 3 dimention to 2 dimention array, here we use dp[2][m][n], rotate track previous and current values.

Further observation, we notice that first row (track previous state), we don't need the whole row values,
we only care about 2 position value: dp[i - 1][j][k] and dp[i - 1][j - count0][k - count1].
so it can be reduced to 2D array. dp[m][n].

- 2D DP definition: dp[m+1][n+1] ~ maximum counts, m is number of 0, n is number of 1
- DP formula： dp[i][j] = max(dp[i][j], dp[i - count0][j - count1] + 1)

> This problem is a variation on the 0-1 Knapsack Problem with a wrinkle:
each item has a 2-dimensional weight, but a constant value.
If we were to naively attempt every single permutation of up to 600 strings, that would be 2^600 permutations.

But thankfully we're not tasked with keeping track of each permutation, but simply the maximum number of items.
This calls for the use of dynamic programming (DP) to reduce the overall complexity
by instead only keeping track of the best results of the various subproblems encountered
while working our way to the eventual answer.

For our DP array (dp),
dp[i][j] will represent the largest number of items that can be added to yield i zeros and j ones.
Thus, our answer will ultimately be dp[M][N].
We'll naturally being doing a bottom-up DP approach,
as we'll be starting with no data and iterating through the input array (S), adding more data to dp as we go.

Since each string in S will require us to iterate through the entirety of dp looking for data to update,
we'll need to do this iteration in a top-down fashion, to avoid interfering with our overall bottom-up approach,
which would occur if we were to update entries that will be the basis for later updates in the same pass.

Once we reach the end, we return dp[M][N].
"""
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        Time Complexity: O(l * m * n) ~ l is strs length[=the number of strings]，m is number of 0，n number of 1
        Space Complexity: O(m * n) ~ dp 2D array
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for cur_string in strs:
            count0 = cur_string.count('0')
            count1 = len(cur_string) - count0

            for i in reversed(range(count0, m + 1)):
                for j in reversed(range(count1, n + 1)):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - count0][j - count1])
        return dp[m][n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
