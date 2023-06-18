class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(None)
        def helper(idx, remAmount):
            if remAmount == 0:
                return 1
            if remAmount < 0 or idx >= len(coins):
                return 0
            
            include = helper(idx, remAmount - coins[idx])
            exclude = helper(idx + 1, remAmount)

            return include + exclude

        return helper(0, amount)

