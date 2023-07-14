class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rows, cols = set(), set()
        firstRowHasZero = False
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                firstRowHasZero = True
        firstColHasZero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstColHasZero = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i != 0 and j != 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstRowHasZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        if firstColHasZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0


        

        
