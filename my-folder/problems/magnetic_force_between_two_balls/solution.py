class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def isInfeasible(force):
            prev = position[0]
            count = 1
            for pos in position[1:]:
                if (pos - prev) >= force:
                    prev = pos
                    count += 1
                
            return count < m
        
        low, high = 0, max(position) - min(position) + 1

        while low < high:
            mid = (low + high) >> 1

            if isInfeasible(mid):
                high = mid
            else:
                low = mid + 1
        
        return low - 1
