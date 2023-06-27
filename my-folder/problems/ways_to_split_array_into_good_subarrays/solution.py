class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        count = 0
        lo = 0
        hi = 0

        while hi < len(nums):
            if nums[hi] == 1:
                if count == 0:
                    count = 1
                else:
                    count *= (hi - lo)
                    count %= (10 ** 9 + 7)
                lo = hi
            hi += 1
        return count

