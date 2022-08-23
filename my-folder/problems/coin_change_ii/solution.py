class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        
        # for i in range(len(coins) + 1):
            # mem[i][0] = 1
        
        # print(mem)
        def helper(target, idx):
            if mem[idx][target] != -1:
                return mem[idx][target]
            
            if target == 0:
                mem[idx][target] = 1 
                return mem[idx][target]
            if idx > len(coins) - 1:
                mem[idx][target] = 0
                return mem[idx][target]
            out = 0
            if coins[idx] <= target:
                out += helper(target - coins[idx], idx)
                out += helper(target, idx + 1)
            else:
                out += helper(target, idx + 1)
            mem[idx][target] = out
            return mem[idx][target]
        return helper(amount, 0)