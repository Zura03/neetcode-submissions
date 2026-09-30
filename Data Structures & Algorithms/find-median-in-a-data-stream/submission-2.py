class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] < num:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        if len(self.small) > 1 + len(self.large):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > 1 + len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0])/2.0
        