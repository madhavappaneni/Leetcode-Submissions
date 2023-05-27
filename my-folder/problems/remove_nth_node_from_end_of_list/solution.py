# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length = 0
        # curr = head
        # if not head.next:
        #     return None
        # while curr:
        #     curr = curr.next
        #     length += 1
        # k = length - n
        # if k == 0:
        #     head = head.next
        #     return head
        # curr = head
        # while k > 1:
        #     curr = curr.next
        #     k -= 1
        # curr.next = curr.next.next if curr and curr.next else None
        # return head

        dummy = ListNode(None)
        dummy.next = head
        slow, fast = dummy, dummy

        for i in range(n + 1):
            fast = fast.next
        
        while slow and fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next if slow and slow.next else None

        return dummy.next