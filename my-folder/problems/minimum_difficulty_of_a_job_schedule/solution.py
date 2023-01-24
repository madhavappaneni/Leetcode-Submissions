class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        n = len(jobDifficulty)
        
        hardestJobs = [0] * n
        hardestTillNow = float('-inf')
        for i in range(n-1, -1, -1):
            hardestTillNow = max(hardestTillNow, jobDifficulty[i])
            hardestJobs[i] = hardestTillNow
        
        @lru_cache(maxsize = None)
        def solve(idx, days):
            if days == d:
                return (hardestJobs[idx])
            hardest = float('-inf')
            best = float('inf')
            for i in range(idx, n - (d - days)):
                hardest = max(hardest, jobDifficulty[i])
                best = min(best , hardest + solve(i + 1, days + 1))
            return best
        
        return solve(0, 1)
                
            