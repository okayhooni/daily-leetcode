"""
https://leetcode.com/problems/coin-change/

> Topic: Dynamic Programming
"""
from typing import List, Dict

INF = float('inf')


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
                return INF

            res = min(
                1 + get_fewest_num_by_amount(target_amount - coin)
                for coin in coins
            )

            dp_fewest_num_by_amount_cache[target_amount] = res

            return res

        res_amount = get_fewest_num_by_amount(amount)
        # print(sorted(dp_fewest_num_by_amount_cache), len(dp_fewest_num_by_amount_cache))
        if res_amount == INF:
            return -1
        return res_amount

    def coinChangeWithDPArray(self, coins: List[int], amount: int) -> int:
        dp_fewest_num_by_amount_cache: List = [None for _ in range(amount + 1)]
        dp_fewest_num_by_amount_cache[0] = 0
        for denomination in coins:
            try:
                dp_fewest_num_by_amount_cache[denomination] = 1
            except IndexError:
                pass

        def get_fewest_num_by_amount(target_amount: int):
            if target_amount < 0:
                return float('inf')

            if dp_fewest_num_by_amount_cache[target_amount] is not None:
                return dp_fewest_num_by_amount_cache[target_amount]

            res = min(
                1 + get_fewest_num_by_amount(target_amount - coin)
                for coin in coins
            )

            dp_fewest_num_by_amount_cache[target_amount] = res

            return res

        res_amount = get_fewest_num_by_amount(amount)
        # print(dp_fewest_num_by_amount_cache, len(dp_fewest_num_by_amount_cache))
        if res_amount == INF:
            return -1
        return res_amount

    def coinChangeWithBitwiseTabulation(self, coins: List[int], amount: int) -> int:
        reachable = 1 << amount
        res = 0

        while reachable & 1 == 0:
            next_reachable = reachable
            for coin in coins:
                next_reachable |= (reachable >> coin)

            # print(bin(reachable), '/', bin(next_reachable))

            if next_reachable == reachable:
                return -1
            reachable = next_reachable
            res += 1
        return res


if __name__ == '__main__':
    test_coins = [1, 2, 5]
    test_amount = 11

    sol = Solution()
    # print(sol.coinChange(test_coins, test_amount))
    # print(sol.coinChange([10, 7, 3, 1], 14))
    print(sol.coinChangeWithBitwiseTabulation([10, 7, 3, 1], 14))
    # print(sol.coinChange([1, 2, 5], 100))
    # print(sol.coinChangeWithDPArray([1, 2, 5], 100))
    # print(sol.coinChangeWithDPArray([1], 0))
    # print(sol.coinChangeWithDPArray([3], 4))
    print(sol.coinChangeWithBitwiseTabulation([3], 4))
