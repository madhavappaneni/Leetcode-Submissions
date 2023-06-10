class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque([])
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        distance = 0
        while queue:
            # print(queue)
            queueLen = len(queue)
            for i in range(queueLen):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(len(rooms)) and col in range(len(rooms[0])) and rooms[row][col] == 2147483647:
                        rooms[row][col] = rooms[r][c] + 1
                        queue.append((row, col))

        
                        

            