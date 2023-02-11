class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pos = defaultdict(int)
        ans = []
        stack = []
        for i, val in enumerate(nums2):
            while stack and nums2[stack[-1]] < val:
                idx = stack.pop()
                pos[nums2[idx]] = val
            stack.append(i)
        for i in nums1:
            ans.append(pos[i] if i in pos else -1)
        return ans
                