class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefixSum = [nums[0]]
        out = []
        if k == 0:
            return nums
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        for i in range(len(nums)):
            if i - k < 0 or i + k >= len(nums):
                out.append(-1)
            else:
                out.append((prefixSum[i + k + 1] - prefixSum[i - k]) // (2 * k + 1))

        return out