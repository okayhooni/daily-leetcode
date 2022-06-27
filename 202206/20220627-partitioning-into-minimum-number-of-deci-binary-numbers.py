"""
https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

> Topic: Math / Greedy Algorithm

Hint)
- Think about if the input was only one digit. Then you need to add up as many ones as the value of this digit.
- If the input has multiple digits, then you can solve for each digit independently,
  and merge the answers to form numbers that add up to that input.
- Thus the answer is equal to the max digit.

Ref) https://dev.to/seanpgallivan/solution-partitioning-into-minimum-number-of-deci-binary-numbers-3njo
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(map(int, set(n)))

    def minPartitionsRef(self, n: str) -> int:
        return int(max(n))


if __name__ == "__main__":
    sol = Solution()
    assert sol.minPartitions("32") == 3
    assert sol.minPartitions("82734") == 8
    assert sol.minPartitions("27346209830709182346") == 9
