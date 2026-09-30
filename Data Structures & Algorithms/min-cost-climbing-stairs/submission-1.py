class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(i, c):
            if i >= len(cost):
                return c

            one = dfs(i + 1, c + cost[i])
            two = dfs(i + 2, c + cost[i])
            return min(one, two)

        return min(dfs(0, 0), dfs(1, 0))