class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-1 * num for num in nums]
        heapify(nums)
        score = 0
        
        while k > 0:
            p = -1 * heappop(nums)
            score += p
            heappush(nums, -1 * ceil(p/3))
            k -= 1
        return score