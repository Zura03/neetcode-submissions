class Solution:
    def climbStairs(self, n: int) -> int:
        
        # def dfs(i):
        #     if i > n:
        #         return 0
            
        #     if i == n:
        #         return 1

        #     return dfs(i + 1) + dfs(i + 2)

        # return dfs(0)


        # cache = [-1] * n

        # def dfs(i):
        #     if i > n:
        #         return 0
            
        #     if i == n:
        #         return 1

        #     if cache[i] != -1:
        #         return cache[i]

        #     cache[i] = dfs(i + 1) + dfs(i + 2)
        #     return cache[i]

        # return dfs(0)

        # dp = [0] * (n + 1)
        # dp[n], dp[n-1] = 1, 1
        # for i in range(n - 2, -1, -1):
        #     dp[i] = dp[i + 1] + dp[i + 2]
        # return dp[0]

        one, two = 1, 1
        for i in range(n - 1):
            one, two = one + two, one
        return one


        