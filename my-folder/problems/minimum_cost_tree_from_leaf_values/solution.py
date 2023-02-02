class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        @lru_cache(None)
        def solve(i, j):
            if j - 1 == i:
                return arr[i] * arr[j]
            if i >= j:
                return 0
            minSum = float('inf')
            for k in range(i, j):
                localSum = solve(i, k) + solve(k + 1, j) + max(arr[i:k+1]) * max(arr[k+1:j+1])
                if localSum != -1:
                    minSum = min(localSum, minSum)
            return minSum if minSum != float('inf') else -1

        return solve(0, len(arr) - 1)