class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            d = point[0]**2 + point[1]**2
            heapq.heappush(distances, [d, point])

        res = []
        while len(res) < k:
            res.append(heapq.heappop(distances)[1])
        return res