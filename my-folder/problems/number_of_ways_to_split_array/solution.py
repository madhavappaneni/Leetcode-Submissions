class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftSum, count, totalSum = 0 , 0, sum(nums)
        for i in range(len(nums) - 1):
            leftSum += nums[i]
            if 2 * leftSum >= totalSum: count += 1
        return count