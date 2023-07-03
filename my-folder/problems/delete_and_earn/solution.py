class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)

        for num in nums:
            points[num] += num

        maxNum = max(nums)

        @lru_cache(None)
        def helper(n):
            if n == 0:
                return 0
            if n == 1:
                return points[1]
            
            return max(helper(n - 1), helper(n - 2) + points[n])
        
        return helper(maxNum)
        