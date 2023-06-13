class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        # def helper(n):
        #     if n == 0 or n == 1 or n == 2:
        #         return n
        #     return helper(n - 1) + helper(n - 2)
        
        # return helper(n)
            
        # memo = [-1] * (n + 1)

        # def helper(n):
        #     if memo[n] != -1:
        #         return memo[n]
            
        #     elif n in [0, 1, 2]:
        #         return n
            
        #     memo[n] = helper(n - 1) + helper(n - 2)
            
        #     return memo[n]
        
        # return helper(n)


        # memo = [-1] * (n + 1)

        # if n <= 2:
        #     return n

        # memo[0], memo[1], memo[2] = 0, 1, 2


        # for i in range(3, n + 1):
        #     memo[i] = memo[i - 1] + memo[i - 2]
        
        # return memo[-1]




        mem = [0, 1]

        if n in [0, 1, 2]:
            return n
        
        for i in range(2, n + 1):
            mem[i % 2] = sum(mem)
        
        return sum(mem)
