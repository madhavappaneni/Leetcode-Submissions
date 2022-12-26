class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0, 1]
        if n == 0 or n == 1 or n ==2:
            return n

        for i in range(2, n + 1):
            mem[i % 2] = sum(mem)
        return sum(mem)

