class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(i, curSum):
            if curSum == amount:
                return 0
            if curSum > amount or i == len(coins):
                return float("inf")
            if (i, curSum) in memo:
                return memo[(i, curSum)]

            # Choose the coin
            take = dfs(i, curSum + coins[i]) + 1
            # Skip the coin
            skip = dfs(i + 1, curSum)

            memo[(i, curSum)] = min(take, skip)
            return memo[(i, curSum)]
        
        res = dfs(0, 0)
        return res if res != float("inf") else -1
