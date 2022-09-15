# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root:
                return False
            left = helper(root.left)
            right = helper(root.right)
            mid = (root == p or root == q)

            if left + right + mid >= 2:
                self.ans = root

            return mid or left or right
        helper(root)
        return self.ans