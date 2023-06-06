class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        h = {}

        for n in nums2[::-1]:
            while stack and stack[-1] < n:
                stack.pop()
            if stack:
                h[n] = stack[-1]
            stack.append(n)
        
        res = []

        for n in nums1:
            if n in h:
                res.append(h[n])
            else:
                res.append(-1)
        
        return res