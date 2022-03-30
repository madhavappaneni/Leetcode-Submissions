class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
        
        while row >= 0 and col >= 0 and row <= len(matrix)-1 and col <= len(matrix[0]) - 1:
            # print(row, col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
            
        return False
                