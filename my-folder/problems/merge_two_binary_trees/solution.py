# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 == None and root2 == None:
            return None
        if root1 == None: return root2
        if root2 == None: return root1
        nodeval = (root1.val if root1 else 0) + (root2.val if root2 else 0)
        res = TreeNode(nodeval)
        if (root1.left or root2.left):
            res.left = self.mergeTrees(root1.left, root2.left)
        if (root1.right or root2.right):
            res.right = self.mergeTrees(root1.right, root2.right)
        return res