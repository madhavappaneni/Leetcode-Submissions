class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        # numsSet = set(nums)
        # self.ans = None

        # def backtrack(currIdx, prev):
        #     if prev not in numsSet and len(prev) == len(nums[0]):
        #         print(prev)
        #         self.ans = prev
        #         return True
        #     if currIdx == len(nums[0]):
        #         return False
            
        #     zero = prev + "0"
        #     one = prev + "1"
        #     return backtrack(currIdx + 1, zero) or backtrack(currIdx + 1, one)
        
        # backtrack(0, "")
        # return self.ans

        ans = []

        for i, x in enumerate(nums):
            if x[i] == '1': ans.append('0')
            else: ans.append('1')
        return "".join(ans)