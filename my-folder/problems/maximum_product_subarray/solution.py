class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        
        maxSoFar = 1
        minSoFar = 1
        
        for num in nums:
            maxSoFar, minSoFar = max(num, maxSoFar * num, minSoFar * num), min(num, maxSoFar * num, minSoFar * num)
            res = max(maxSoFar, res)
        
        return res
                