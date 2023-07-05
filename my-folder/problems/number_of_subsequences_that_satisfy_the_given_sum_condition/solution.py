class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # nums.sort()

        # start, end = 0, len(nums) - 1
        # count = 0
        # mod = 10 ** 9 + 7

        # while start <= end:
        #     if nums[start] + nums[end] <= target:
        #         count = (count + pow(2, end - start, mod)) % mod
        #         start += 1
        #     else:
        #         end -= 1
        
        # return count

        nums.sort()
        mod = 10 ** 9 + 7
        ans = 0
        for leftIdx in range(len(nums)):
            leftVal = nums[leftIdx]
            reqVal = target - leftVal
            rightIdx = bisect.bisect_right(nums, reqVal) - 1
            if rightIdx >= leftIdx:
                ans += pow(2, rightIdx - leftIdx, mod)
        
        return ans % mod 