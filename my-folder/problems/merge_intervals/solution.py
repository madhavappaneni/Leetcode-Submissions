class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        intervals.sort()
        for interval in intervals:
            if not out or interval[0] > out[-1][1]:
                out.append(interval)
            else:
                out[-1][1] = max(out[-1][1], interval[1])
        
        return out