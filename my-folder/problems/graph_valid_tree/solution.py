class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
            return True
        else:
            return False
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
        

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        if len(edges) != n - 1: return False
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return False
        return True
        