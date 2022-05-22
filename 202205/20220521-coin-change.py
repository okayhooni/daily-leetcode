"""
https://leetcode.com/problems/coin-change/

> Topic: Dynamic Programming
"""
from typing import List, Dict
from collections import namedtuple, deque

INF = float('inf')
CoinIdxAmountPair = namedtuple('CoinIdxAmountPair', ('coin_idx', 'amount'))


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

    def coinChangeWithTabulation(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort()
        dp_fewest_num_by_amount_cache = [INF for _ in range(amount + 1)]
        dp_fewest_num_by_amount_cache[0] = 0
        for coin in coins:
            try:
                dp_fewest_num_by_amount_cache[coin] = 1
            except IndexError:
                pass

        for cur_amount in range(1, amount):
            for coin in coins:
                next_amount = cur_amount + coin
                if next_amount > amount:
                    break
                dp_fewest_num_by_amount_cache[next_amount] = min(dp_fewest_num_by_amount_cache[next_amount],
                                                                 dp_fewest_num_by_amount_cache[cur_amount] + 1)

        return dp_fewest_num_by_amount_cache[amount] if dp_fewest_num_by_amount_cache[amount] != INF else -1

    def coinChangeWithBitwiseTabulation(self, coins: List[int], amount: int) -> int:
        reachable = 1 << amount
        res = 0

        while reachable & 1 == 0:
            next_reachable = reachable
            for coin in coins:
                next_reachable |= (reachable >> coin)
                # bit-wise tabulation with sliding window (two-pointer) approach

            # print(bin(reachable), '/', bin(next_reachable))

            if next_reachable == reachable:
                return -1
            reachable = next_reachable
            res += 1
        return res

    def coinChangeWithCombination(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()  # SORTING IS NECESSARY

        coin_types_len = len(coins)
        candidate_coin_pairs_on_cur_level = [CoinIdxAmountPair(0, 0)]
        level_by_used_num_of_coins = 0
        visited = set()
        while candidate_coin_pairs_on_cur_level:
            level_by_used_num_of_coins += 1
            tmp = []
            for coin_idx, coin_amount in candidate_coin_pairs_on_cur_level:
                for cur_coin_idx in range(coin_idx, coin_types_len):  # COMBINATIONS WITHOUT DUPLICATIONS
                    cur_amount = coin_amount + coins[cur_coin_idx]
                    if cur_amount == amount:
                        return level_by_used_num_of_coins
                    elif cur_amount > amount:
                        break
                    elif cur_amount not in visited:
                        visited.add(cur_amount)
                        tmp.append(CoinIdxAmountPair(cur_coin_idx, cur_amount))

            candidate_coin_pairs_on_cur_level = tmp
        return -1

    def coinChangeWithBFS(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        moves = sorted(coins)
        len_moves = len(coins)
        # bfs
        queue = deque([CoinIdxAmountPair(0, 0)])
        # queue = deque([0])
        visited = set()
        level_by_used_num_of_coins = 0
        while queue:
            for _ in range(len(queue)):
                coin_idx, coin_amount = queue.popleft()

                for cur_coin_idx in range(coin_idx, len_moves):  # COMBINATIONS
                    next_amount = coin_amount + moves[cur_coin_idx]
                    if next_amount > amount:
                        break
                    elif next_amount == amount:
                        return level_by_used_num_of_coins + 1
                    elif next_amount not in visited:
                        queue.append(CoinIdxAmountPair(cur_coin_idx, next_amount))
                        visited.add(next_amount)

            level_by_used_num_of_coins += 1

        return -1


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
    print(sol.coinChangeWithBFS([186, 419, 83, 408], 6249))
