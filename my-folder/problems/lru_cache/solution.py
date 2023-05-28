class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next, self.prev = None, None
    

class LRUCache:
    def __init__(self, capacity: int):
        self.LRUCache = { }
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node) -> None:
        prevRight = self.right.prev
        prevRight.next = node
        node.prev = prevRight
        node.next = self.right
        self.right.prev = node
    
    def remove(self, node) -> None:
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            self.remove(self.LRUCache[key])
            self.insert(self.LRUCache[key])
            return self.LRUCache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            self.remove(self.LRUCache[key])
        node = Node(key, value)
        self.insert(node)
        self.LRUCache[key] = node

        if self.capacity < len(self.LRUCache):
            lru = self.left.next
            self.remove(lru)
            del self.LRUCache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)