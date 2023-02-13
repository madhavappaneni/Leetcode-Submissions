class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # h = defaultdict(int)

        # for idx, n in enumerate(nums):
        #     if target - n in h:
        #         return idx, h[target-n]
        #     else:
        #         h[n] = idx

        for i in range(0, len(nums) + 1):
            diff = target-nums[i]
            if diff in nums and not i == nums.index(diff):
                return [i, nums.index(diff)]