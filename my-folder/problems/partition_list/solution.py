# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lDummy = ListNode(0, None)
        rDummy = ListNode(0, None)

        lHead = lDummy
        rHead = rDummy

        curr = head

        while curr:
            temp = curr.next
            curr.next = None
            if curr.val < x:
                lHead.next = curr
                lHead = lHead.next
            else:
                rHead.next = curr
                rHead = rHead.next
            curr = temp

        lHead.next = rDummy.next

        return lDummy.next
        