class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap, res = [], []
        L, R = 0, 0
        while R < k:
            heapq.heappush(heap, [-nums[R], R])
            R += 1
        res.append(-heap[0][0])
        for R in range(k, len(nums)):
            heapq.heappush(heap, [-nums[R], R])
            L += 1
            while heap[0][1] < L:
                heapq.heappop(heap)
            res.append(-heap[0][0])

        return res

            