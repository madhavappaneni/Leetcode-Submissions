class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # dp = [1] * (len(nums))
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        
        # def solve(idx, prev):
        #     print(idx, prev, 'test')
        #     if mem[idx][prev + 1] != None:
        #         return mem[idx][prev + 1]
        #     if idx == len(nums):
        #         return 0
        #     taken = 0
        #     if prev == -1 or nums[prev] < nums[idx] :
        #         taken =  1 + solve(idx + 1, idx)
        #     notTaken = solve(idx + 1, prev)
        #     mem[idx][prev + 1] = max(taken, notTaken)
        #     return mem[idx][prev + 1]
        # n = len(nums)
        # mem = [[None] * (n + 1) for _ in range(n + 1)]
        # return solve(0, -1)

        sub = [nums[0]]

        for num in nums:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = bisect_left(sub, num)
                sub[i] = num
        return len(sub)












