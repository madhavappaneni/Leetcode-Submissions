class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums = tuple(nums)
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        N = len(nums)

        curr = [False] * (target + 1)

        curr[0] = True
        prev = curr.copy()
        
        for currNum in nums:
            for j in range(currNum, target + 1):
                curr[j] = prev[j] or prev[j - currNum]
            prev = curr.copy()

        return prev[-1]
