class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # n = len(nums)

        # for i in range(len(nums)):

        #     while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            
        
        # for i in range(len(nums)):
        #     if nums[i] != i + 1:
        #         return i + 1
            

        # return n + 1

            n = len(nums)

            if 1 not in nums:
                return 1

            for i in range(n):
                if nums[i] <= 0 or nums[i] > n:
                    nums[i] = 1

            for i in range(n):
                a = abs(nums[i])

                if a == n:
                    nums[0] = - abs(nums[0])
                else:
                    nums[a] = - abs(nums[a])

            for i in range(1, n):
                if nums[i] > 0:
                    return i

            if nums[0] > 0:
                return n

            return n + 1