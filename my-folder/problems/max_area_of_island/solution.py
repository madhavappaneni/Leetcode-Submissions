class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(r, c):
            if not(r in range(len(grid)) and c in range(len(grid[0])) and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        seen = set()
        
        return max(dfs(i, j) 
                    for i in range(len(grid)) 
                    for j in range(len(grid[0])))
