# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root is None:
                return True, 0
            leftBalanced, leftHeight = helper(root.left)
            rightBalanced, rightHeight = helper(root.right)
            return (leftBalanced and rightBalanced and abs(leftHeight - rightHeight) < 2), (1 + max(leftHeight, rightHeight))
        return helper(root)[0]
        