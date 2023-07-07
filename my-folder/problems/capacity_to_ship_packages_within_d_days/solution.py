class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isInFeasible(cap):
            currCap = 0
            numTrips = 0

            for weight in weights:
                if weight + currCap <= cap:
                    currCap = currCap + weight
                else:
                    currCap = weight
                    numTrips += 1
            
            return numTrips >= days


        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) >> 1

            if isInFeasible(mid):
                low = mid + 1
            else:
                high = mid
        
        return low
