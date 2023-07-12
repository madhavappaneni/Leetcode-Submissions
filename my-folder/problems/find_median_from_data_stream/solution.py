class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []
    
    def rebalanceHeaps(self):
        if self.large and self.small and self.large[0] < -1 * self.small[0]:
            heappush(self.large, -1 * heappop(self.small))
        if len(self.small) - len(self.large) > 1:
            heappush(self.large, -1 * heappop(self.small))
        if len(self.large) - len(self.small) > 1:
            heappush(self.small, -1 * heappop(self.large))

    def addNum(self, num: int) -> None:
        heappush(self.small, -1 * num)
        self.rebalanceHeaps()

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (self.large[0] - self.small[0])/2
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -self.small[0]
        

# class MedianFinder:

#     def __init__(self):
#         self.data = []
#         self.dataLen = 0

#     def addNum(self, num: int) -> None:
#         insertIdx = bisect_left(self.data, num)
#         self.data.insert(insertIdx, num)
#         self.dataLen += 1


#     def findMedian(self) -> float:
#         if self.dataLen % 2 == 0:
#             return (self.data[self.dataLen // 2] + self.data[self.dataLen // 2 - 1]) / 2
#         else:
#             return self.data[self.dataLen // 2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()