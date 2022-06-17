# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root == None:
                return 0
            if root.left and not root.left.left and not root.left.right:
                return root.left.val + helper(root.right)
            return helper(root.left) + helper(root.right)
        return helper(root)
