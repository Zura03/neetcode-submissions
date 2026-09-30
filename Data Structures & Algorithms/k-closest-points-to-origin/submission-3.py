class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(distances, [dist, point])
        
        res = []
        while k > 0:
            d, p = heapq.heappop(distances)
            res.append(p)
            k -= 1
        return res