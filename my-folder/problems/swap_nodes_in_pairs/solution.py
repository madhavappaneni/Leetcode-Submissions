# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(None, head)
        # curr = head
        # prev = dummy
        
        # while curr and curr.next:
        #     first, second = curr, curr.next

        #     prev.next, first.next, second.next = second, second.next, first

        #     prev = first
        #     curr = first.next

        # return dummy.next

        
        if not head or not head.next:
            return head

        first = head
        second = head.next


        first.next = self.swapPairs(second.next)
        second.next = first
        return second