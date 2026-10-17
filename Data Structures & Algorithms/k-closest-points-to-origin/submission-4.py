class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[pow(p[0], 2) + pow(p[1], 2), i] for i, p in enumerate(points)]
        print(dist)
        heapq.heapify(dist)
        res = []
        while k > 0:
            idx = heapq.heappop(dist)[1]
            print(idx)
            res.append(points[idx])
            k -= 1
        return res
