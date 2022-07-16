"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        curr = head
        if curr is None:
            retNode = Node(insertVal)
            retNode.next = retNode
            return retNode
        print(curr.val)
        prev = curr
        curr = curr.next
        inserted = False
        while curr != head:
            if prev.val <= insertVal <= curr.val:
                inserted = True
                prev.next = Node(insertVal)
                prev.next.next = curr
                break
            elif prev.val > curr.val and prev.val < insertVal and insertVal > curr.val:
                inserted = True
                prev.next = Node(insertVal)
                prev.next.next = curr
                break
            elif prev.val > curr.val and prev.val > insertVal and insertVal < curr.val:
                inserted = True
                prev.next = Node(insertVal)
                prev.next.next = curr
                break
            prev = curr
            curr = curr.next
        if not inserted:
            temp = Node(insertVal)
            temp.next = prev.next
            prev.next = temp
        return head