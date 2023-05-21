class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff = float('inf')
        ans = None
        for pivot in range(len(nums)):

            left, right = pivot + 1, len(nums) - 1

            while left < right:
                threeSum = nums[pivot] + nums[right] + nums[left]

                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    return target
                
                if abs(threeSum - target) < minDiff:
                    ans = threeSum
                    minDiff = abs(threeSum - target)
        return ans
