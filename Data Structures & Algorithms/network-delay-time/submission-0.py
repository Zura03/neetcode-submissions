class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for u, v, t in times:
            adj[u].append([v, t])

        shortest = {}

        q = [[0, k]]
        res = 0
        while q:
            w1, n1 = heapq.heappop(q)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            res = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(q, [w1 + w2, n2])

        for node in adj.keys():
            if node not in shortest:
                return -1
        return res

        