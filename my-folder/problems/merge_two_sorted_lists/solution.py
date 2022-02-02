# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head3 = tail3 = ListNode()
        
        while list1 and list2:
            if list1.val > list2.val:
                tail3.next = list2
                list2 = list2.next
            else:
                tail3.next = list1
                list1 = list1.next
            tail3 = tail3.next

        tail3.next = list2 if not list1 else list1
        
        return head3.next