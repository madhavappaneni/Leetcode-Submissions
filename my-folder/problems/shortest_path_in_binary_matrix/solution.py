class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW_MAX = len(grid) - 1
        COL_MAX = len(grid[0]) - 1
        directions = [(-1, 0), (-1, -1), (0, -1), (1, 0),
                      (1, -1), (-1, 1), (1, 1), (0, 1)]

        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        def getNeighbors(row, col):
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row > ROW_MAX or new_col < 0 or new_col > COL_MAX or grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)

        queue = collections.deque()
        queue.append((0, 0))
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (ROW_MAX, COL_MAX):
                return distance
            for nei_row, nei_col in getNeighbors(row, col):
                grid[nei_row][nei_col] = distance + 1
                queue.append((nei_row, nei_col))
        return -1