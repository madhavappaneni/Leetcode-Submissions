class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def calculateSlope(point1, point2):
            return (point2[1] - point1[1]) / (point2[0] - point1[0]) if point1[0] != point2[0] else float('inf')

        if len(points) == 1:
            return 1

        result = 2

        for i in range(len(points)):
            c = collections.defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    point1 = points[i]
                    point2 = points[j]
                    slope = calculateSlope(point2, point1)
                    c[slope] += 1
            result = max(result, max(c.values()) + 1)

        return result