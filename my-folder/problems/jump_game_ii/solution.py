class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # @lru_cache(None)
        # def helper(idx):
        #     if idx >= len(nums) - 1:
        #         return 0
            
        #     minValue = float('inf')
        #     for i in range(idx + 1, min(len(nums) - 1, idx + nums[idx]) + 1):
        #         val = helper(i)
        #         if val != -1:
        #             minValue = min(minValue, val)

        #     return minValue + 1 if minValue != float('inf') else -1
        # return helper(0)

        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res