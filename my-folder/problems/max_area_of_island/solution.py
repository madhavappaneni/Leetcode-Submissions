class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        nrows, ncols = len(grid), len(grid[0])
        maxArea = 0
        area = 0
        def dfs(i, j):
            nonlocal area
            if i < 0 or j < 0 or i >= nrows or j >= ncols or (i,j) in visited or grid[i][j] != 1:
                return area
            visited.add((i,j))
            area += 1
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            return
        
        for i in range(nrows):
            for j in range(ncols):
                if (i, j) not in visited and grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    maxArea = max(area, maxArea)
        return maxArea