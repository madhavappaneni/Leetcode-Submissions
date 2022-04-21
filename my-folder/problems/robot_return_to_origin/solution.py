class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counts = Counter(moves)
        print(counts)
        counts_u = counts['U'] if 'U' in counts else 0
        counts_d = counts['D'] if 'D' in counts else 0        
        counts_l = counts['L'] if 'L' in counts else 0                
        counts_r = counts['R'] if 'R' in counts else 0                        
        return counts_u == counts_d and counts_l == counts_r
