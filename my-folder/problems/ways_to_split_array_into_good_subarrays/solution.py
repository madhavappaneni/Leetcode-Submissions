class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        i = 0
        count = 0
        zerosCount = 0

        while i < len(nums) and nums[i] != 1:
            i += 1

        while i < len(nums):
            if nums[i] == 0:
                zerosCount += 1
            elif nums[i] == 1:
                if count == 0:
                    count = 1
                if zerosCount > 0:
                    count *= (zerosCount + 1) % (10 ** 9 + 7)
                zerosCount = 0
            i += 1
        return count % (10 ** 9 + 7)

