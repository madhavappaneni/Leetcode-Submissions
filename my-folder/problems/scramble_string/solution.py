class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @lru_cache(maxsize = None)
        def solve(s1, s2):
            if s1 == s2:
                return True
            n, m = len(s1), len(s2)
            if n != m or Counter(s1) != Counter(s2):
                return False
            f = solve
            for k in range(1, n):
                if (f(s1[:k], s2[:k]) and f(s1[k:], s2[k:])) or (f(s1[:k], s2[-k:]) and f(s1[k:], s2[:-k])):
                    return True
            return False
        return solve(s1, s2)

        