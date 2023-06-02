class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        h = []

        for num in nums:
            heapq.heappush(h, int(num))
            # print(h)
            if len(h) > k:
                heapq.heappop(h)
        
        return str(h[0])
            