class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        out = [[None]* n for i in range(m)]
        
        if m * n != len(original):
            return []
        
        for i in range(0, m):
            for j in range(0, n):
                out[i][j] = original[i*n + j]
        
        return out