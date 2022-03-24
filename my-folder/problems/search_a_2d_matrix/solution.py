class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_start, row_end, row_num = 0, len(matrix) - 1, 0
    
        while row_start <= row_end:
            row_mid = row_start + (row_end - row_start) // 2

            if matrix[row_mid][0] == target:
                row_num = row_mid
                break
            elif matrix[row_mid][0] > target:
                row_end = row_mid - 1
            else:
                row_start = row_mid + 1

            row_num = row_end


        col_start, col_end, col_num = 0, len(matrix[0]) - 1, 0

        while col_start <= col_end:
            col_mid = col_start + (col_end - col_start) // 2
            # print(col_mid, col_start, col_end, matrix[row_num][col_mid])
            if matrix[row_num][col_mid] == target:
                # return row_num, col_mid
                return True

            elif matrix[row_num][col_mid] > target:
                col_end = col_mid - 1

            else:
                col_start = col_mid + 1
            # print(col_mid, col_start, col_end)
        # return -1
        return False