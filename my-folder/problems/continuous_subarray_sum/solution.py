class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        h = {0: 0}
        currSum = 0

        for i, val in enumerate(nums):
            currSum += val

            if currSum % k not in h:
                h[currSum % k] = i + 1
            
            elif h[currSum % k] < i:
                return True

        return False
            
