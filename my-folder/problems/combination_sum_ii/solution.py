class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []
        def dfs(rem, path, idx):
            if rem == 0:
                out.append(path[:])
                return
            elif rem < 0:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(rem - candidates[i], path, i + 1)
                path.pop()
                # dfs(rem, path, i + 1)
                
        dfs(target, [], 0)
        
        return out
                