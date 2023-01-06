class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        currSum = 0
        h = defaultdict(int)
        h[0] = -1
        for idx, num in enumerate(nums):
            # print(idx, currSum, currSum %k, h)
            currSum += num
            if currSum % k not in h:
                h[currSum % k] = idx
            elif idx - h[currSum % k] >= 2:
                return True
        return False