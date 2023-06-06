class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 2

        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1

            while nums[i] >= nums[j]:
                j -= 1
            
            print(i, j)
            nums[i], nums[j] = nums[j], nums[i]

        start, end = i + 1, len(nums) - 1

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
