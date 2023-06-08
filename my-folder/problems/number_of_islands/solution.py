class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid) - 1
        COLS = len(grid[0]) - 1
        
        def dfs(r, c):
            if not (0 <= r <= len(grid) - 1) \
             or not (0 <= c <= len(grid[0]) - 1) \
             or grid[r][c] == "0" \
             or (r, c) in visited:
                return
            visited.add((r, c))
            
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            
            return

        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    count += 1
        return count