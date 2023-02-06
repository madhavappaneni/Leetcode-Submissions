class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        mat[:] = [[0] * (n + 1)] + [[0] + row for row in mat]
        res = [[0] * n for _ in range(m)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                mat[i][j] += mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
        for i in range(m):
            for j in range(n):
                r1, r2 = max(0, i - k), min(i + k + 1, m)
                c1, c2 = max(0, j - k), min(j + k + 1, n)
                res[i][j] = mat[r2][c2] + mat[r1][c1] - mat[r2][c1] - mat[r1][c2]
        return res