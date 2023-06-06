class UnionFind:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.root = [None] * (nVertices)
        for i in range(len(self.root)):
            self.root[i] = i
        
    def find(self, x):
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootX:
                    self.root[i] = rootY
    
    def connected(self, x, y):
        return self.root[x] == self.root[y]

    def getRootSetLen(self):
        return len(set(self.root))

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for u in range(n):
            for v in range(n):
                if u != v and isConnected[u][v] == 1 and not uf.connected(u, v):
                    uf.union(u, v)
        
        return uf.getRootSetLen()
        
