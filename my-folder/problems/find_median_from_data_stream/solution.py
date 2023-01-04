class MedianFinder:

    def __init__(self):
        self.small = [] #stores values < median
        self.large = [] #stores values > mediam

    def rebalanceHeaps(self):
        # The following order is important
        if self.large and self.small and -1 * self.small[0] > self.large[0]:
            heappush(self.large, -1 * heappop(self.small))

        if len(self.large) - len(self.small) > 1:
            heappush(self.small, -1 * heappop(self.large))
        
        if len(self.small) - len(self.large) > 1:
            heappush(self.large, -1 * heappop(self.small))



    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        self.rebalanceHeaps()
        

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (self.large[0] - self.small[0]) / 2
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -1 * self.small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()