class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        def helper(currentIndex, currArr):
            out.append(currArr.copy())
            for i in range(currentIndex, len(nums)):
                if i != currentIndex and nums[i] == nums[i - 1]:
                    continue
                currArr.append(nums[i])
                helper(i + 1, currArr)
                currArr.pop()
                    
        helper(0, [])
    
        return out