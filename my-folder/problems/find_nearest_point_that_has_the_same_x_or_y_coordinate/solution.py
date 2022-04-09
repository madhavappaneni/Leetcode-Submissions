class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDist = 1000000000
        point = None
        for i in range(len(points)-1, -1, -1):
            if points[i][0] == x or points[i][1] == y:
                dist = abs(x-points[i][0]) + abs(y-points[i][1])
                # print(i, dist)
                if dist <= minDist:
                    minDist = dist
                    point = i
        return point if point != None else -1
