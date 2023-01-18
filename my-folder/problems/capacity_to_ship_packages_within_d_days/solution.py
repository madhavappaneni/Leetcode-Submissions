class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            nDays = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:
                    nDays += 1
                    total = weight
            return nDays <= days

        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) >> 1

            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low