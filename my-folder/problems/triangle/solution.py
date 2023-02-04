class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        @lru_cache(None)
        def solve(level, idx):
            if level == len(triangle) - 1:
                return triangle[level][idx]
            ans = triangle[level][idx] + min(solve(level + 1, idx), solve(level + 1, idx + 1))
            return ans
        
        return solve(0, 0)