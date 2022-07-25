class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        # def dfs(i, j):
        #     # print(i, j)
        #     if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
        #         return
        #     grid[i][j] = "#"
        #     dfs(i-1, j)
        #     dfs(i+1, j)
        #     dfs(i, j+1)
        #     dfs(i, j-1)
        #     return
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            visited.add((i, j))
            while q:
                r, c = q.popleft()
                for (dr, dc) in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visited:
                        q.append((row, col))
                        visited.add((row, col))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs(i, j)
                    count += 1    
       
        return count