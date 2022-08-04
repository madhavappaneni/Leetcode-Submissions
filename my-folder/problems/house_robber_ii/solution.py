class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        firstMax, secondMax = 0, 0
        dp = [0] * (n + 1)
        first, second = nums[0], max(nums[0], nums[1])
        
        for i in range(2, n-1):
            current = max(first + nums[i], second)
            first = second
            second = current
        firstMax = second
        
        if n > 2:
            first, second = nums[1], max(nums[1], nums[2])
            for i in range(3, n):
                current = max(first + nums[i], second)
                first = second
                second = current

            secondMax = second
    
        return max(firstMax, secondMax)