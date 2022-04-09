class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [(self.squared_distance(i), i) for i in points]
        heapq.heapify(h)
        return [a[1] for a in heapq.nsmallest(k, h)]
    
    def squared_distance(self, point):
        return point[0] ** 2 + point[1] ** 2