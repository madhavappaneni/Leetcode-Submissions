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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        maxVertex = 0
        graph = collections.defaultdict(list)
        for edge in edges:
            maxVertex = max(maxVertex, edge[0], edge[1])
        uf = UnionFind(maxVertex + 1)
        ans = None
        for edge in edges:
            if uf.connected(edge[0], edge[1]):
                return edge
            uf.union(edge[0], edge[1])
        return
