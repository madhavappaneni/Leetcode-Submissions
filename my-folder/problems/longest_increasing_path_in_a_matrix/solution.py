class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        outDeg = [[0] * n for _ in range(m)]
    
        directions = [[0, 1],
                        [0, -1],
                        [-1, 0],
                        [1, 0]]

        for r in range(m):
            for c in range(n):
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row in range(m) and \
                        col in range(n) and \
                        matrix[row][col] > matrix[r][c]:
                        outDeg[r][c] += 1

        queue = deque([])
        for r in range(m):
            for c in range(n):
                if outDeg[r][c] == 0:
                    queue.append((r, c))
        
        lipLength = 0
        
        while queue:
            lipLength += 1
            queueLength = len(queue)
            for i in range(queueLength):
                r, c = queue.popleft()
                temp = matrix[r][c]
                if temp == '#':
                    continue
                matrix[r][c] = "#"

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(m) and \
                        col in range(n) and \
                        matrix[row][col] != "#" and \
                        matrix[row][col] < temp:
                        outDeg[row][col] -= 1
                        if outDeg[row][col] == 0:
                            queue.append((row, col))
        
        return lipLength