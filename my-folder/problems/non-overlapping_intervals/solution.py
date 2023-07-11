class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key = lambda x: x[1])

        # currEnd = intervals[0][1]

        # count = 0
        # for interval in intervals[1:]:
        #     if interval[0] >= currEnd:
        #         currEnd = interval[1]
        #     else:
        #         count += 1
        # return count 
        
        # count = 0
        # intervals.sort()
        # currEnd = float('-inf')
        # for interval in intervals:
        #     if interval[0] >= currEnd:
        #         currEnd = interval[1]
        #     else:
        #         count += 1
        #         currEnd = min(interval[1], currEnd)
        # return count
        count = 0
        intervals.sort(key = lambda x:x[1])
        currEnd = float('-inf')
        for interval in intervals:
            if interval[0] >= currEnd:
                currEnd = interval[1]
            else:
                count += 1
        return count







