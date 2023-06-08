class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        directions = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]

        def getNeighbors(row, col):
            neis = []
            for dr, dc in directions:
                newR, newC = row + dr, col + dc
                if 0 <= newR < n and 0 <= newC < n and grid[newR][newC] == 0:
                    neis.append([newR, newC])
            return neis

        # def getNeighbors(row, col):
        #     for row_difference, col_difference in directions:
        #         new_row = row + row_difference
        #         new_col = col + col_difference
        #         if not(0 <= new_row <= n - 1 and 0 <= new_col <= n - 1):
        #             continue
        #         if grid[new_row][new_col] != 0:
        #             continue
        #         yield (new_row, new_col)
        
        queue = deque([[0, 0]])

        grid[0][0] = 1

        while queue:
            r, c = queue.popleft()
            currDistance = grid[r][c]

            if r == n - 1 and c == n - 1:
                return currDistance

            for neiR, neiC in getNeighbors(r, c):
                grid[neiR][neiC] = currDistance + 1
                queue.append([neiR, neiC])

        return -1
