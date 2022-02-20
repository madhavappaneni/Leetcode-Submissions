class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(1, num+1):
            s = sum([int(j) for j in str(i)]) % 2 == 0
            if s % 2 != 0:
                ans+=(1)
        return ans
            