class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.count = size
    
    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
            self.count -= 1
        return self.count

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])
        uf = UnionFind(n)
        if len(logs) < n - 1:
            return -1
        for log in logs:
            unionOut = uf.union(log[1], log[2])
            if unionOut == 1:
                return log[0]
        return -1
            
        