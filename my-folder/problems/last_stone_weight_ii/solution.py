class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = {0}
        for st in stones:
            print(s)
            tmp = set()
            for i in s:
                tmp.add(abs(i + st))
                tmp.add(abs(i - st))
            s = tmp
        return min(s)