class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maxLen = 1
        prev = nums[0]
        currLen = 1

        for num in nums[1:]:
            if num == prev + 1:
                currLen += 1
                maxLen = max(maxLen, currLen)
            elif num == prev:
                continue
            else:
                currLen = 1
            prev = num
        return maxLen