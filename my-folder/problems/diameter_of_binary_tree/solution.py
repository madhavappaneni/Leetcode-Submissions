# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(node): # diameter, height
            if not node:
                return 0, -1
            
            ld, lh = helper(node.left)
            rd, rh = helper(node.right)

            return max(ld, rd, lh + rh + 2), 1 + max(lh, rh)
        
        return helper(root)[0]
            
