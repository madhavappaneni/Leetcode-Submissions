class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        subset = []
        n = len(nums)
        nums.sort()
        def dfs(first=0):
            if first == k:
                out.append(subset[:])
                return
            if first > k:
                return
            
            for i in range(first, n):
                if i > first and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
                
        for k in range(n + 1):
            dfs()
        return out