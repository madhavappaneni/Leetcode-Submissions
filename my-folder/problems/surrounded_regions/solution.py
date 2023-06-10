class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(r, c):
            if r not in range(len(board)) or c not in range(len(board[0])) or board[r][c] != 'P':
                return
            
            board[r][c] = 'O'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
            return

        borderZeros = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    if i in [0, len(board) - 1] or j in [0, len(board[0]) - 1]:
                        borderZeros.add((i, j))
                    board[i][j] = 'P'
        
        for r, c in borderZeros:
            dfs(r, c)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'P':
                    board[i][j] = 'X'
        