class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            v = heapq.heappop(nums)
            heapq.heappush(nums, v + 1)
        res = 1
        for v in nums:
            res = int((res * v) % (1e9+7))
        return res