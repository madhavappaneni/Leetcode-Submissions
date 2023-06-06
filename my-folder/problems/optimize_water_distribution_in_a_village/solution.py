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
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        uf = UnionFind(n + 1)
        possibleEdges = []
        possibleEdges.extend(pipes)
        possibleEdges.extend([[0, idx + 1, val] for idx, val in enumerate(wells)])
        possibleEdges.sort(key = lambda x:x[2])

        totalCost = 0

        for u, v, cost in possibleEdges:
            if not uf.connected(u, v):
                uf.union(u, v)
                totalCost += cost
        return totalCost
