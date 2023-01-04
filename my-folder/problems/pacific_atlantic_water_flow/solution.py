class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        
        def pacificCrawl(row, col, currVal):
            if row < 0 or col < 0 or row > len(heights) - 1 or col > len(heights[0]) - 1:
                return
            if heights[row][col] < currVal or (row, col) in pacific:
                return
            pacific.add((row, col))
            directions = [[-1,0], [1,0], [0, 1], [0, -1]]
            for dr, dc in directions:
                pacificCrawl(row + dr, col + dc, heights[row][col])

        def atlanticCrawl(row, col, currVal):
            if row < 0 or col < 0 or row > len(heights) - 1 or col > len(heights[0]) - 1:
                return
            if heights[row][col] < currVal or (row, col) in atlantic:
                return
            atlantic.add((row, col))
            directions = [[-1,0], [1,0], [0, 1], [0, -1]]
            for dr, dc in directions:
                atlanticCrawl(row + dr, col + dc, heights[row][col])

        ROWS = len(heights)
        COLS = len(heights[0])
        for i in range(0, ROWS):
            pacificCrawl(i, 0, heights[i][0])
            atlanticCrawl(i, COLS - 1, heights[i][COLS - 1])

        for i in range(0, COLS):
            pacificCrawl(0, i, heights[0][i])
            atlanticCrawl(ROWS - 1, i, heights[ROWS - 1][i])

        # print(pacific)
        # print(atlantic)
        return [val for val in pacific if val in atlantic]