class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row_min, col_min, row_max, col_max = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        # target_row = None

        # while row_min <= row_max:
        #     row_mid = (row_min + row_max) >> 1
        #     if matrix[row_mid][0] <= target <= matrix[row_mid][-1]:
        #         target_row = row_mid
        #         break
        #     elif matrix[row_mid][0] > target:
        #         row_max = row_mid - 1
        #     else:
        #         row_min = row_mid + 1
        # if target_row is None:
        #     return False

        # while col_min <= col_max:
        #     col_mid = (col_min + col_max) >> 1
        #     if matrix[target_row][col_mid] == target:
        #         return True
        #     elif matrix[target_row][col_mid] > target:
        #         col_max = col_mid - 1
        #     else:
        #         col_min = col_mid + 1
            
        # return False

        m = len(matrix)
        n = len(matrix[0])

        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) >> 1
            midElement = matrix[mid // n][mid % n]
            if midElement == target:
                return True
            elif midElement > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False




























            