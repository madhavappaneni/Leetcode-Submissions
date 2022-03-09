class Solution:
    def minimumSum(self, num: int) -> int:
        sNum = sorted(str(num))
        return int(sNum[0] + sNum[2]) + int(sNum[1] + sNum[3])