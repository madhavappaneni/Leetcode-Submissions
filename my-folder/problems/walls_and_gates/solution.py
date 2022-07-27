class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        ROWS, COLS = len(rooms), len(rooms[0])
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append((i,j))
        while q:
            for i in range(len(q)):
                r, c = q.pop()
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row not in range(ROWS) \
                    or col not in range(COLS) \
                    or rooms[row][col] == -1:
                        continue
                    elif rooms[row][col] > rooms[r][c] + 1:
                        rooms[row][col] = rooms[r][c] + 1
                        q.append((row, col))