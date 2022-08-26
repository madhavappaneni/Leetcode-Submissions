class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insertIndex = len(intervals)
        for i, interval in enumerate(intervals):
            # print(i, interval)
            if interval[0] > newInterval[0]:
                insertIndex = i
                break
        intervals.insert(insertIndex, newInterval)
        # print(intervals)
        
        out = []
        for interval in intervals:
            if not out or out[-1][1] < interval[0]:
                out.append(interval)
            else:
                out[-1][1] = max(out[-1][1], interval[1])
        return out