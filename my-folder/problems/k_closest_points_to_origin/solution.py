class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        
        def measureDistance(point):
            return (point[0] ** 2 + point[1] ** 2)
        
        for point in points:
            heapq.heappush(h, [-1 * measureDistance(point), point])
            if len(h) > k: heapq.heappop(h)
            
        return [x[1] for x in h]

