class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # out = []
        # insertIdx = len(intervals)
        # for i, currInterval in enumerate(intervals):
        #     if currInterval[0] > newInterval[0]:
        #         insertIdx = i
        #         break
        insertIdx = bisect_left(intervals, newInterval) 
        intervals.insert(insertIdx, newInterval)

        out = []

        for interval in intervals:
            if not out or interval[0] > out[-1][1]:
                out.append(interval)
            else:
                out[-1][1] = max(out[-1][1], interval[1])
        
        return out
            
            

