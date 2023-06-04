class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        out = []

        def helper(currentIdx, currentPrefix):
            out.append(currentPrefix.copy())

            for i in range(currentIdx, len(nums)):
                helper(i + 1, currentPrefix + [nums[i]])
            
            return
        
        helper(0, [])

        return out