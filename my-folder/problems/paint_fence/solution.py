class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        two_down = k
        one_down = k * k
        for i in range(3, n + 1):
            curr = (one_down + two_down) * (k - 1)
            two_down = one_down
            one_down = curr
        return one_down