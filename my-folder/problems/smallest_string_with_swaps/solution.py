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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))

        for u, v in pairs:
            uf.union(u, v)

        h = defaultdict(list)
        out = [None] * len(s)
        for idx, val in enumerate(uf.root):
            root = uf.find(val)
            h[root].append(idx)

        for vals in (h.values()):
            for i, val in zip((vals), sorted([s[i] for i in vals])):
                out[i] = val
        
        return ''.join(out)
                




















