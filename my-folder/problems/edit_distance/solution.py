class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(None)
        def solve(i, j):
            if i == 0:
                return j
            elif j == 0:
                return i
            elif word1[i - 1] == word2[j - 1]:
                return solve(i - 1, j - 1)
            else:
                return min(solve(i-1, j), solve(i, j-1), solve(i-1, j-1)) + 1
        
        return solve(len(word1), len(word2))