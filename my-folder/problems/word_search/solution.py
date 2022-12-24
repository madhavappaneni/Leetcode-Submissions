class Solution:

    def helper(self, row, col, suffix, board):
            if len(suffix) == 0:
                return True
            if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1 or board[row][col] != suffix[0]:
                return False
            temp = board[row][col]
            board[row][col] = '#'
            res = self.helper(row+1 , col, suffix[1:], board) or self.helper(row , col + 1, suffix[1:], board) or self.helper(row-1 , col, suffix[1:], board) or self.helper(row , col-1, suffix[1:], board)
            board[row][col] = suffix[0]
            return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for  j in range(len(board[0])):
                if self.helper(i, j, word, board):
                    return True
        return False
            