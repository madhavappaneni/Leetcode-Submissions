class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        # return sum([nums[i] + nums[i+1] if i % 2 == 0 else None for i in range(len(nums))])
        ans = 0
        for i in range(0, len(nums), 2):
           ans += nums[i]
        return ans