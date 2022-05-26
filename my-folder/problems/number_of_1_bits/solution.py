class Solution:
    def hammingWeight(self, n: int) -> int:
        n = int(bin(n)[2:])
        count = 0
        while n>0:
            c = n % 10
            if c == 1:
                count += 1
            n = n // 10
        return count