class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isBlockValid(block):
            block = [i for i in block if i != '.']
            return len(block) == len(set(block))
            
        def areRowsValid():
            for row in board:
                if not isBlockValid(row):
                    return False
            return True

        def areColsValid():
            for col in zip(*board):
                if not isBlockValid(col):
                    return False
            return True

        def areSubBoardsValid():
            for i in range(0, 7, 3):
                for j in range(0, 7, 3):
                    subBoard = [board[m][n] for m in range(i, i + 3) for n in range(j, j + 3)]
                    if not isBlockValid(subBoard):
                        return False
            return True
        
        return areRowsValid() and areColsValid() and areSubBoardsValid()
