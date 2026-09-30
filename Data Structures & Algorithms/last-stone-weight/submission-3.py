class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            first, second = heapq.heappop(heap), heapq.heappop(heap)
            if second > first:
                heapq.heappush(heap, first - second)
        
        return -heap[0] if heap else 0