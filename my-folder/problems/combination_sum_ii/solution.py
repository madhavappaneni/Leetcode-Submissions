class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()
        def helper(currArr, remTarget, currIndex):
            if remTarget < 0:
                return
            elif remTarget == 0:
                out.append(currArr.copy())
            for i in range(currIndex, len(candidates)):
                if candidates[i] == candidates[i-1] and i != currIndex:
                    continue
                currArr.append(candidates[i])
                helper(currArr, remTarget - candidates[i], i + 1)
                currArr.pop()
        helper([], target, 0)
        return out
