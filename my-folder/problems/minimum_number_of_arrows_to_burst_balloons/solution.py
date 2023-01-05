class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        currEnd = float('-inf')
        count = 0
        for point in points:
            if point[0] <= currEnd:
                continue
            else:
                currEnd = point[1]
                count += 1
        return count
            