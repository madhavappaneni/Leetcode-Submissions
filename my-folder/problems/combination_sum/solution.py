class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []

        def helper(currIdx, currCandidate, currTarget):
            if currTarget == 0:
                out.append(currCandidate[:])
                return
            
            if currTarget < 0:
                return
            
            for i in range(currIdx, len(candidates)):
                currCandidate.append(candidates[i])
                helper(i, currCandidate, currTarget - candidates[i])
                currCandidate.pop()
            
            return
        
        helper(0, [], target)

        return out
