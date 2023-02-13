class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        ans = []
        direction = 0

        while len(ans) < len(matrix) * len(matrix[0]):
            if direction == 0:
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])
                top += 1
            if direction == 1:
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            if direction == 3:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

            direction = (direction + 1) % 4
        return (ans)