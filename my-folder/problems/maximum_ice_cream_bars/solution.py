class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if coins-cost < 0:
                return count
            coins = coins-cost
            count += 1
        return count
            
