class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        # left = [0] * len(nums)
        # right = [0] * len(nums)

        # for i in range(len(nums)):
        #     if i == 0:
        #         left[i] = 0
        #     else:
        #         left[i] = left[i-1] + nums[i-1]

        # for i in range(len(nums) - 1, -1, -1):
        #     if i == len(nums) - 1:
        #         right[i] = 0
        #     else:
        #         right[i] = right[i + 1] + nums[i + 1]
        
        # for i in range(len(nums)):
        #     if left[i] == right[i]:
        #         return i

        # return -1

        left, right = 0, sum(nums)
        for i in range(len(nums)):
            if i == 0:
                left = 0
                right -= nums[i]
            elif i == len(nums) - 1:
                right = 0
                left += nums[i - 1]
            else:
                left += nums[i-1]
                right -= nums[i]
            if left == right:
                return i
        return -1


            




















