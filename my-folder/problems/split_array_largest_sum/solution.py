class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isInFeasible(tresh):
            total = 0
            count = 1
            for num in nums:
                total += num
                if total > tresh:
                    count += 1
                    total = num
            return count > k

        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) >> 1
            if isInFeasible(mid):
                low = mid + 1
            else:
                high = mid
        return low
