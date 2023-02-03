class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        nums = [1] + nums + [1]

        @lru_cache(None)
        def solve(i, j):
            if i > j:
                return 0
            maxAns = 0
            for k in range(i, j + 1):
                localAns = solve(i, k - 1) + solve(k + 1, j) + nums[i - 1] * nums[k] * nums[j + 1]
                maxAns = max(maxAns, localAns)
            return maxAns
        
        return solve(1, len(nums) - 2)

