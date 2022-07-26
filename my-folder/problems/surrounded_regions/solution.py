class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nRows, nCols = len(board), len(board[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or i == nRows or j == nCols or board[i][j] != "O":
                return
            board[i][j] = "T"
            
            dfs(i, j-1)
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j+1)
        
        
        for i in range(nRows):
            for j in range(nCols):
                if (i in [0, nRows - 1] or j in [0, nCols - 1]) and board[i][j] == "O":
                        dfs(i, j)
        for i in range(nRows):
            for j in range(nCols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
                
        
                    