"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        deq = collections.deque()
        deq.append(root)
        while deq:
            size = len(deq)
            for i in range(size):
                elem = deq.popleft()
                if i < size - 1:
                    elem.next = deq[0]
                if elem.left: 
                    deq.append(elem.left)
                if elem.right:
                    deq.append(elem.right)
        return root