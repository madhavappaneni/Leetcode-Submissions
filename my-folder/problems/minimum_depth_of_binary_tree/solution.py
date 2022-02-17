# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if not root:
            return 0
        else:
            deq = deque()
            deq.append((1, root))
            
            while deq:
                level, node = deq.popleft()
                left, right = node.left, node.right
                
                if left == None and right == None:
                    return level
                
                if left:
                    deq.append((level+1, left))
                if right:
                    deq.append((level+1, right))
                               
               
                               
                             