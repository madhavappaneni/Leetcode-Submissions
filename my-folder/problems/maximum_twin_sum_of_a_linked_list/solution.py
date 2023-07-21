# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        self.curr = head
        self.maxVal = float('-inf')

        def helper(node):
            if not node:
                return
            helper(node.next)
            self.maxVal = max(self.curr.val + node.val, self.maxVal)
            self.curr = self.curr.next
        
        helper(head)
        return self.maxVal
