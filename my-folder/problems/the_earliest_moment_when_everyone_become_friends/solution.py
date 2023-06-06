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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        logs.sort()
        count = n
        # Initially there are n groups
        # If all groups are friends, in the end, there would be 1 group
        for time, u, v in logs:
            if not uf.connected(u, v):
                uf.union(u,v)
                count -= 1
                if count == 1:
                    return time
        return -1
