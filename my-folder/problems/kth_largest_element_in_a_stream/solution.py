class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.pq = nums
        self.k = k
        
        while len(self.pq) > self.k:
            heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k: heapq.heappop(self.pq)
        
        return self.pq[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)