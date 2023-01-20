class TrieNode:
    def __init__(self, val = None, score = 0):
        self.val = val
        self.score = score
        self.edges = {}
        self.isEnd = False
class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.h = {}

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        found = self.h[key] if key in self.h else 0
        self.h[key] = val
        for char in key:
            if char not in curr.edges:
                curr.edges[char] = TrieNode(char)
            curr.edges[char].score += (val - found)
            # print(key, val, char, found, val - found, curr.edges[char].score)
            curr = curr.edges[char]
        
        curr.isEnd = True

    def find(self, key):
        curr = self.root
        for char in key:
            if char not in curr.edges:
                return 0
            curr = curr.edges[char]
        return curr.score if curr.isEnd else 0
    
    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.edges:
                return 0
            curr = curr.edges[char]
        # print(prefix, curr.val, curr.score)
        return curr.score

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)