# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2_ = None
        head2 = head2_
        sum = 0
        head = head.next
        while head:
            if head.val == 0 and sum != 0:
                node2 = ListNode(sum)
                sum = 0
                if head2 is not None:
                    head2.next = node2
                    head2 = head2.next
                else:
                    head2_ = node2
                    head2 = head2_
            else:
                sum += head.val

            head = head.next

        return head2_