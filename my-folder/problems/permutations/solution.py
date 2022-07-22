class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        n = len(nums)
        def dfs(first):
            if first == n:
                out.append(nums[:])
            
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                dfs(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        dfs(0)
        return out