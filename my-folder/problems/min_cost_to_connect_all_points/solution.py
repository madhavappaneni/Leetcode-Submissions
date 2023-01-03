class UnionFind:
    def __init__(self, size):
        self.root = [None] * size
        self.rank = [1] * size
        for i in range(size):
            self.root[i] = i
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def connected(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        return rootX == rootY
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = UnionFind(len(points))
        count = len(points) - 1
        edges = []
        visited = set()
        heapq.heapify(edges)
        visited.add(0)
        def getManhattanDistance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        for i in range(1, len(points)):
            heapq.heappush(edges, (getManhattanDistance(points[0], points[i]), (0, i)))
        out = 0
        
        while edges and count > 0:
            # print(edges, visited)
            edge = heapq.heappop(edges)
            point1 = edge[1][0]
            point2 = edge[1][1]
            cost = edge[0]
            if point2 not in visited:
                out += cost
                # print(cost)
                visited.add(point2)
                for j in range(len(points)):
                    if j not in visited:
                        heapq.heappush(edges, (getManhattanDistance(points[point2], points[j]), (point2, j)))

                count -= 1
        return out
        
        
#         def getValidEdgesFrom(point):
#             edges = []
#             for i in range(len(points)):
#                 if i in visited or i == point:
#                     continue
#                 distance = getManhattanDistance(points[i], points[point])
#                 edges.append([distance, (i, point)])
#             heapq.heapify(edges)
#             return edges
        
        
        