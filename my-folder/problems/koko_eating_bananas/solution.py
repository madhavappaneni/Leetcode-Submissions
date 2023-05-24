class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def inFeasible(speed):
            numHours = sum([math.ceil(pile/speed) for pile in piles])
            return numHours > h

        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) >> 1
            if inFeasible(mid):
                low = mid + 1
            else:
                high = mid

        return low
