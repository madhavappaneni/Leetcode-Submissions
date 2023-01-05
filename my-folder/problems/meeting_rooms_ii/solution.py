class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = [intervals[0][1]]
        heapify(rooms)

        for interval in intervals[1:]:
            if interval[0] >= rooms[0]:
                heappop(rooms)
            
            heappush(rooms, interval[1])
        return len(rooms)

