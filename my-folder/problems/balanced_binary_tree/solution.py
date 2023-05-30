# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if node is None:
                return True, 0
            leftBalanced, leftHeight = helper(node.left)
            rightBalanced, rightHeight = helper(node.right)
            return (leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1), 1 + max(leftHeight, rightHeight)
        
        return helper(root)[0]
        
        