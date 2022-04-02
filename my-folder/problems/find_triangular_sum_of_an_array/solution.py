class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        ans = 0

        for l in range(len(nums)-1, -1, -1):
            for i in range(l):
                nums[i] = (nums[i] + nums[i+1]) % 10
        return (nums[0])