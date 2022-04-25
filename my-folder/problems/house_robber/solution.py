class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        mem = [0] * (len(nums))
        mem[0] = nums[0]
        mem[1] = nums[1]
        
        for i in range(2, len(nums)):
            for j in range(i-1):
                mem_j = mem[j]
                mem[i] = max(mem[i], nums[i] + mem_j)
            
        # print(mem)
        return max(mem)
        