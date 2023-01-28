class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSubArray = maxSubArray = float('-inf')

        for num in nums:
            currSubArray = max(num, currSubArray + num)
            maxSubArray = max(maxSubArray, currSubArray)
        
        return maxSubArray
