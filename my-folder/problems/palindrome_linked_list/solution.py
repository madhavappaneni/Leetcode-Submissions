# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.curr = head

        def palindromeHelper(node):
            if node:
                if not palindromeHelper(node.next):
                    return False
                if node.val != self.curr.val:
                    return False
                self.curr = self.curr.next
            return True
        return palindromeHelper(head)
