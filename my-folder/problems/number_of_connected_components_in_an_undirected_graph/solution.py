class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
    
    def find(self, x):
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootX:
                    self.root[i] = rootY
        return
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return len(set(uf.root))
            