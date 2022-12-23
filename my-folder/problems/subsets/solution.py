class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def helper(counter, prefix):
            # print('test', counter, prefix)
            output.append(prefix.copy())
            for i in range(counter, len(nums)):
                prefix.append(nums[i])
                helper(i + 1, prefix)
                prefix.pop()

            return
        helper(0, [])
        return output