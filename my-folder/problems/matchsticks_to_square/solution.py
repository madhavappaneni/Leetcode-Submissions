class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        edgeLen = sum(matchsticks) / 4

        if int(edgeLen) != edgeLen:
            return False

        sides = [0,0,0,0]
        matchsticks.sort(reverse=True)

        def backtrack(currIdx):
            if currIdx == len(matchsticks):
                return True
            
            for i in range(4):
                if sides[i] + matchsticks[currIdx] > edgeLen:
                    continue

                sides[i] += matchsticks[currIdx] 
                if backtrack(currIdx + 1):
                    return True

                sides[i] -= matchsticks[currIdx]
            
            return False
        
        return backtrack(0)
        