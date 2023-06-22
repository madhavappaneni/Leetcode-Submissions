class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = float('-inf')

        for num in nums:
            currSum = max(currSum, 0) + num
            maxSum = max(maxSum, currSum)
        
        return maxSum