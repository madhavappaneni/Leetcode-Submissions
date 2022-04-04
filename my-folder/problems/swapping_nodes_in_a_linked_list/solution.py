# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        master_head = head
        curr = head
        count = 0
        while head:
            head = head.next
            count += 1
        
        head = curr
        first = None
        second = None
        p = 1
        while head:
            if p == k:
                first = head
            if p == count - k + 1:
                second = head
            head = head.next
            p += 1
        first.val, second.val = second.val, first.val
        return master_head