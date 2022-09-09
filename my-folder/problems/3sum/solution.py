class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for pivot in range(len(nums)):
            if pivot > 0 and nums[pivot] == nums[pivot - 1]:
                continue
            left, right = pivot + 1, len(nums) - 1
            while left < right:
                threeSum = nums[pivot] + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([nums[pivot], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res