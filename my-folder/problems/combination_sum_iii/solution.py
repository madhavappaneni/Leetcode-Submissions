class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        
        def dfs(target, path, idx):
            if target == 0 and len(path) == k:
                output.append(list(path))
                return
            elif target < 0 or len(path) == k:
                return
            
            for i in range(idx, 9):
                path.append(i+1)
                dfs(target - i - 1, path, i + 1)
                path.pop()
            
        dfs(n, [], 0)
        
        return output
                
            
            
                