class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a = text1
        b = text2
        mem = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
        pi = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

        for i in range(len(a)+1):
            for j in range(len(b)+1):
                if i == 0 or j == 0:
                    mem[i][j] = 0
                    pi[i][j] = 'b'
                    continue
                if a[i-1] == b[j-1]:
                    mem[i][j] = mem[i-1][j-1] + 1
                    pi[i][j] = 'd'
                elif mem[i][j-1] >= mem[i-1][j]:
                    mem[i][j] = mem[i][j-1]
                    pi[i][j] = 'l'
                else:
                    mem[i][j] = mem[i-1][j]
                    pi[i][j] = 'u'
        return (mem[len(a)][len(b)])
