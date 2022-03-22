class Solution:
    def findComplement(self, num: int) -> int:
        binary = ""
        from collections import deque
        binary = []

        while num > 0:
            rem = num % 2
            num = num // 2
            binary.append(rem)

        ans = 0

        for i in range(len(binary)-1, -1, -1):
            ans += (2 ** i) *abs(1-binary[i])

        return ans