class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(1, n + 1)}

        for u, v, t in times:
            adj[u].append((t, v))

        q = []
        heapq.heappush(q, [0, k])
        visit = set()
        res = 0
        while q:
            w1, n1 = heapq.heappop(q)
            if n1 in visit:
                continue
            for w2, n2 in adj[n1]:
                heapq.heappush(q, [w1 + w2, n2])
            visit.add(n1)
            res = w1

        return res if len(visit) == n else -1
        