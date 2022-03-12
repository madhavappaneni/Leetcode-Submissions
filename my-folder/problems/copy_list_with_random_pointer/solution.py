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
        curr = head
        head2 = Node(0)
        curr2 = head2
        h = {}
        while curr:
            curr2.next = Node(curr.val, curr.next, None)
            h[curr] = curr2.next
            curr = curr.next
            curr2 = curr2.next
        # print(h)
        curr2 = head2.next
        curr = head
        while curr2:
            if curr.random:
                curr2.random = h[curr.random]
            curr2 = curr2.next
            curr = curr.next
        
        return head2.next