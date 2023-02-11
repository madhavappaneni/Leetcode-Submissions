class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                p = stack.pop()
                ans[p] = n
            stack.append(i)
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                p = stack.pop()
                ans[p] = n
        return ans
