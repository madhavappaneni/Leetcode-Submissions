class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        target = sum(matchsticks) / 4
        if target != int(target): return False
        k = 4
        sides = [0] * k
        matchsticks.sort(reverse=True)
        def helper(currIdx):
            if currIdx == len(matchsticks):
                return True
            for j in range(k):
                if sides[j] + matchsticks[currIdx] > target: continue
                sides[j] += matchsticks[currIdx]
                if helper(currIdx + 1): return True
                sides[j] -= matchsticks[currIdx]
        return helper(0)
        

