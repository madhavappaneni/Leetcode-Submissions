class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        
        @lru_cache(None)
        def solve(amount, idx):
            if idx >= n:
                return 0
            
            if amount == 0:
                return 1
            
            if amount < 0:
                return 0
            
            return solve(amount - coins[idx], idx) + solve(amount, idx + 1)
        
        return solve(amount, 0)
                