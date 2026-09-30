class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)

        # def dfs(i):
        #     if i >= n:
        #         return 0

        #     return cost[i] + min(dfs(i + 1), dfs(i + 2))        

        # return min(dfs(0), dfs(1))

        # cache = [-1] * len(cost)
        # n = len(cost)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if cache[i] != -1:
        #         return cache[i]

        #     cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     return cache[i]

        # return min(dfs(0), dfs(1))

        #[10, 15, 20] 0
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        return min(cost[0], cost[1])