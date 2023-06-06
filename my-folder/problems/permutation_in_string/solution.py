class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        h1 = defaultdict(int)
        for c in s1:
            h1[c] += 1
        h2 = defaultdict(int)
        for i in range(len(s1)):
            h2[s2[i]] += 1
        if h1 == h2:
            return True 

        for i in range(len(s1), len(s2)):
            if h2[s2[i-len(s1)]] > 1:
                h2[s2[i-len(s1)]] -= 1
            else:
                del h2[s2[i-len(s1)]]
            h2[s2[i]] += 1
            if h1 == h2:
                return True 
        
        return False