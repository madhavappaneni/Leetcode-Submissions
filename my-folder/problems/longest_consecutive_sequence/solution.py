class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        heapify(nums)
        prev = float('-inf')
        count = 1
        maxCount = float('-inf')

        while nums:
            curr = heappop(nums)
            # print(prev, curr, maxCount)
            if prev == curr:
                continue
            elif prev + 1 == curr:
                count += 1
                maxCount = max(count, maxCount)
            else:
                count = 1
                maxCount = max(count, maxCount)
            prev = curr
        
        return maxCount
