class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(target, path, idx):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return
            
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                dfs(target - candidates[i], path, i)
                path.pop()
            
        dfs(target, [], 0)
        
        return result