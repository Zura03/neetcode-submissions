class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for u, v, cost in flights:
            adj[u].append([cost, v])

        res = float("inf")
        visit = set()

        def dfs(K, node, cur):
            nonlocal res
            if node == dst:
                res = min(res, cur)
                return
            if K < 0 or node in visit or cur >= res:
                return

            visit.add(node)
            for cost, d in adj[node]:
                dfs(K - 1, d, cur + cost) 
            visit.remove(node) 

        dfs(k, src, 0)
        return res if res != float("inf") else -1
