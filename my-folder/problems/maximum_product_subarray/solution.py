class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxSoFar = 1
        minSoFar = 1 
        result = float('-inf')

        for num in nums:
            maxSoFar, minSoFar = max(num, num * maxSoFar, num * minSoFar), min(num, num * minSoFar, num * maxSoFar)
            result = max(maxSoFar, result)

        return result


                