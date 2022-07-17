"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = curr = head
        h = {}
        
        newDummy = newCurr = Node(0)
        
        while curr:
            newCurr.next = Node(curr.val, curr.next)
            h[curr] = newCurr.next
            newCurr = newCurr.next
            curr = curr.next

        newCurr = newDummy.next
        curr = head
        
        while newCurr and curr:
            if curr.random:
                newCurr.random = h[curr.random]
            newCurr = newCurr.next
            curr = curr.next
        return newDummy.next
