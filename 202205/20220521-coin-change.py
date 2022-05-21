"""
https://leetcode.com/problems/coin-change/

> Topic: Dynamic Programming
"""
from typing import List, Dict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_fewest_num_by_amount_cache: Dict[int, int] = {
            denomination: 1 for denomination in coins
        }
        dp_fewest_num_by_amount_cache[0] = 0

        def get_fewest_num_by_amount(target_amount: int):
            if target_amount in dp_fewest_num_by_amount_cache:
                return dp_fewest_num_by_amount_cache[target_amount]

            if target_amount < 0:
                return float('inf')

            res = min(
                1 + get_fewest_num_by_amount(target_amount - coin)
                for coin in coins
            )

            dp_fewest_num_by_amount_cache[target_amount] = res

            return res

        res_amount = get_fewest_num_by_amount(amount)
        if res_amount == float('inf'):
            return -1
        return res_amount


if __name__ == '__main__':
    test_coins = [1, 2, 5]
    test_amount = 11

    sol = Solution()
    print(sol.coinChange(test_coins, test_amount))
    print(sol.coinChange([10, 7, 3, 1], 14))
