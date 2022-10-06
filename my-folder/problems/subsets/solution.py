class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first, curr):
            out.append(curr[:])
            for idx in range(first, len(nums)):
                curr.append(nums[idx])
                backtrack(idx + 1, curr)
                curr.pop()
        out = []
        backtrack(0, [])
        return out