class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        oneDown = 0
        twoDown = 0
        
        for i in range(2, len(cost) + 1):
            one = oneDown + cost[i-1]
            two = twoDown + cost[i-2]
            oneDown, twoDown = min(one, two), oneDown
        
        return oneDown