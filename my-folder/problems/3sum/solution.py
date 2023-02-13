class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for pivot in range(len(nums)):
            if pivot > 0 and nums[pivot] == nums[pivot - 1]:
                continue
            target = -1 * nums[pivot]
            start, end = pivot + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == target:
                    ans.append([nums[pivot], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                else:
                    start += 1
        return ans