class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        time = 0

        while queue and fresh > 0:
            q_len = len(queue)    

            for i in range(q_len):
                r, c = queue.popleft()
                dirs = [[0,1], [0,-1], [-1,0], [1,0]]

                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if newR in range(ROWS) and newC in range(COLS) and grid[newR][newC] == 1:
                        queue.append([newR, newC])
                        grid[newR][newC] = 2
                        queue.append((newR, newC))
                        fresh -= 1
            time += 1
    
        return time if fresh == 0 else -1


















