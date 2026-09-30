class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n + 2)
        
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if dp[i] != 0:
                return dp[i]

            dp[i] = dfs(i + 1) + dfs(i + 2)
            return dp[i]

        return dfs(0)