# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rem = 0
        sum_list = ListNode(0)
        sum_tail = sum_list
        while l1 or l2 or rem:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + rem
            rem = 1 if (sum >= 10) else 0
            div = sum % 10
            sum_tail.next = ListNode(div)
            sum_tail = sum_tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return sum_list.next
            