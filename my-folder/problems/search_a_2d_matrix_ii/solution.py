class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def helper(rowStart, rowEnd, colStart, colEnd):

            if (rowStart > rowEnd or colStart > colEnd):
                return False

            rowMiddle = (rowStart + rowEnd) >> 1
            colMiddle = (colStart + colEnd) >> 1

            # print(colMiddle, rowMiddle)

            if matrix[rowMiddle][colMiddle] == target:
                return True

            elif matrix[rowMiddle][colMiddle] > target:
                return helper(rowStart, rowEnd, colStart, colMiddle - 1) \
                    or helper(rowStart, rowMiddle - 1, colMiddle,  colEnd)

            else:
                return helper(rowStart, rowEnd, colMiddle + 1, colEnd) \
                    or helper(rowMiddle + 1, rowEnd, colStart, colMiddle)

        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return False
        return helper(0, m - 1, 0, n - 1)