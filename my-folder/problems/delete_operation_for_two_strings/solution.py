class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a, b = len(word1), len(word2)
        mem = [[0] * (b+1) for _ in range(a + 1)]

        for i in range(a):
            for j in range(b):
                if word1[i] == word2[j]:
                    mem[i+1][j+1] = 1 + mem[i][j]
                else:
                    mem[i+1][j+1] = max(mem[i+1][j], mem[i][j+1])

        return a + b - 2 * mem[a][b]
