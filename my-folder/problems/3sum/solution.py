class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for pivot in range(len(nums)):
            if pivot > 0 and nums[pivot] == nums[pivot-1]:
                continue
            h = {}
            i = pivot + 1
            while i < len(nums):
                complement =  -1 * nums[pivot] - nums[i]

                if complement in h:
                    res.append([nums[pivot], nums[i], complement])
                    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                        i += 1
                h[nums[i]] = i
                i += 1
        return res
            