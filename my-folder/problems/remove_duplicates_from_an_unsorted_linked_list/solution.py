# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        curr = head
        h = defaultdict(int)
        while curr:
            h[curr.val] += 1
            curr = curr.next        
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr and curr.next:
            if curr.next.val in h and h[curr.next.val] > 1:
                curr.next = curr.next.next  
            else:
                curr = curr.next
        return dummy.next