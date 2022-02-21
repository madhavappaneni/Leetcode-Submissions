class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
            
        def compare(num1, num2):
            sum1 = num1 + num2
            sum2 = num2 + num1
            
            return -11 if sum1 > sum2 else 1
            
        nums = sorted(nums, key = cmp_to_key(compare))
        return str(int(''.join(nums)))
        