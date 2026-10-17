class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ns = [-n for n in nums]
        heapq.heapify(ns)

        while k > 0:
            res = heapq.heappop(ns)
            k -= 1
        return -res
        # time complexity : n + klogn
        