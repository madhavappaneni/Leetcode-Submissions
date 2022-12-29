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
    def getRootArr(self):
        return self.root

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for pair in pairs:
            uf.union(pair[0], pair[1])
        rootCharMap = collections.defaultdict(list)
        roots = set(uf.getRootArr())
        for idx, elem in enumerate(uf.getRootArr()):
            elemRoot = uf.find(elem)
            rootCharMap[elemRoot].append(idx)
        out = [None] * len(s)
        for (idx, (k, v)) in enumerate(rootCharMap.items()):
            charArr = [s[i] for i in v]
            charArr.sort()
            j = 0
            for i in v:
                out[i] = charArr[j]
                j += 1
        return ''.join(out)

            
        
        