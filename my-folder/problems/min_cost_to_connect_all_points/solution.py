class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = []

        point1 = points[0]

        for i in range(1, len(points)):
            point2 = points[i]
            dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
            heappush(pq, (dist, 0, i))

        count = len(points) - 1
        visited = [False] * len(points) 
        result = 0
        visited[0] = True
        while pq and count > 0:
            dist, point1, point2 = heappop(pq)
            if not visited[point2]:
                result += dist
                visited[point2] = True
                for j in range(len(points)):
                    if not visited[j]:
                        distance = abs(points[point2][0] - points[j][0]) + \
                                   abs(points[point2][1] - points[j][1])
                        heappush(pq, (distance, point2, j))
                count -= 1
        return result


