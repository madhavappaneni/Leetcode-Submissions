class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        currMax = intervals[0][1]
        print(intervals)
        count = 1
        for interval in intervals[1:]:
            print(interval[0], currMax)
            if interval[0] >= currMax:
                currMax = interval[1]
                count += 1
        
        return len(intervals) - count
