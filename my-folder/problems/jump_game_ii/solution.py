class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        count = 0
        while right < n - 1:
            maxJump = right
            for i in range(left, right + 1):
                maxJump = max(maxJump, nums[i] + i)
            left = right + 1
            right = maxJump
            count += 1
        return count