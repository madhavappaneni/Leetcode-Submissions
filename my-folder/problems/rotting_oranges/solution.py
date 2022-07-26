class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = 0 
        fresh = 0
        time = 0
        ROWS, COLS = len(grid), len(grid[0])
        deq = deque()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    deq.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        # print(deq)
        while deq and fresh > 0:
            for i in range(len(deq)):
                row, col = deq.popleft()
                directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    # print(row, col, r, c, range(ROWS), range(COLS))
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1:
                        grid[r][c] = 2
                        deq.append((r,c))
                        fresh -= 1
                # print(grid)
            time += 1
        # print(deq, time, fresh, grid)
        return time if fresh == 0 else -1