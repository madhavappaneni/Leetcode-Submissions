class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        def helper(first, nums):
            print(first, nums)
            if first == len(nums):
                out.append(nums[:])
            lookup = set()

            for i in range(first, len(nums)):
                if nums[i] not in lookup:
                    nums[i], nums[first] = nums[first], nums[i]
                    helper(first + 1, nums)
                    nums[i], nums[first] = nums[first], nums[i]
                    lookup.add(nums[i])
        helper(0, nums)
        return out
            