class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []

        def helper(remTarget, startIndex, currArr):
            if remTarget < 0 or startIndex > len(candidates) - 1:
                return
            elif remTarget == 0:
                out.append(currArr.copy())
            else:
                for idx in range(startIndex, len(candidates)):
                    currArr.append(candidates[idx])
                    helper(remTarget-candidates[idx], idx, currArr)
                    currArr.pop()
        helper(target, 0, [])
        return out
