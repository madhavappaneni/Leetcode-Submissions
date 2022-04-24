class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        h = {}
        for num_elem in nums:
            for num in num_elem:
                if num in h:
                    h[num] += 1
                else:
                    h[num] = 1
        
        ans = []
        for i in h:
            # print(i, h[i])
            if h[i] == len(nums):
                ans.append(i)
        return sorted(ans)