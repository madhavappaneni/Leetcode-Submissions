# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    curr = None
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.isPalin = True
        
        self.curr = head
        
        def helper(currRec):
            if currRec:
                helper(currRec.next)
                # print(currRec.val,self.curr.val)
                if currRec.val != self.curr.val:
                    self.isPalin = False
                self.curr = self.curr.next

        helper(head)
        return self.isPalin
