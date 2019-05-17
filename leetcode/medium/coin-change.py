class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        result = 999999999999

        def solve(target):
            nonlocal cache
            nonlocal result

            if target < 0:
                return -1

            if target == 0:
                return 0

            if target - 1 in cache:
                return cache[target - 1]

            min_target = 999999999
            for coin in coins:
                res = solve(target - coin)

                if res >= 0 and res < min_target:
                    min_target = 1 + res

            cache[target - 1] = -1 if min_target == 999999999 else min_target
            return cache[target - 1]

        return solve(amount)
