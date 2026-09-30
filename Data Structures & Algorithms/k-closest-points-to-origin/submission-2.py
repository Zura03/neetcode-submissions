class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for point in points:
            d = point[0]**2 + point[1]**2
            heapq.heappush(dist, [d, point])
        
        res = []
        while k > 0:
            res.append(heapq.heappop(dist)[1])
            k -= 1
        return res

        