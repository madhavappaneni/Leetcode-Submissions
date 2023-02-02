class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @lru_cache(None)
        def solve(i, j):
            if i + 1 == j:
                return 0
            minAns = float('inf')
            for idx in range(i + 1, j):
                localAns = solve(i, idx) + solve(idx, j) + values[i] * values[idx] * values[j]
                if localAns != -1:
                    minAns = min(minAns, localAns)
            return minAns if minAns != float('inf') else -1

        return solve(0, len(values) - 1)
            