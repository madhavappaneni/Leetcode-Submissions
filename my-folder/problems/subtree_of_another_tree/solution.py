# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            if self.checkIfSame(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def checkIfSame(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot:
            return root.val == subRoot.val and self.checkIfSame(root.left, subRoot.left) and self.checkIfSame(root.right, subRoot.right)
        
