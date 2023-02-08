class Solution:
    def jump(self, nums: List[int]) -> int:
        currIdx = 0
        count = 0
        high = 0
        while high < len(nums) - 1:
            maxIdx = 0
            for i in range(currIdx, high + 1):
                maxIdx = max(maxIdx, i + nums[i])
            currIdx = high + 1
            high = maxIdx
            count += 1
        
        return count
            