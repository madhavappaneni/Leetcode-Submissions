class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()

        def helper(currIdx, currCandidate, currTarget):
            if currTarget == 0:
                out.append(currCandidate[:])
                return
            
            if currTarget < 0:
                return
            
            for i in range(currIdx, len(candidates)):
                if i != currIdx and candidates[i] == candidates[i - 1]:
                    continue
                currCandidate.append(candidates[i])
                helper(i + 1, currCandidate, currTarget - candidates[i])
                currCandidate.pop()
            return
        
        helper(0, [], target)

        return out
