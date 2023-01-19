class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(day):
            count = 0
            total = 0
            for b in bloomDay:
                if b <= day:
                    total += 1
                    if total >= k:
                        count += 1
                        total = 0
                else:
                    total = 0
            return count >= m

        if m * k > len(bloomDay):
            return -1

        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) >> 1
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
