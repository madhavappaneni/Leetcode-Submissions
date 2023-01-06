class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currSum = 0
        h = defaultdict(int)

        for num in nums:
            currSum += num

            if currSum == k:
                count += 1
            
            count += h[currSum - k]

            h[currSum] += 1
            
        return count