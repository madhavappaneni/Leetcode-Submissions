# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.minDepthHelper(root)
        
    def minDepthHelper(self, node):
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return 1
        
        if node.left == None:
            return 1 + self.minDepthHelper(node.right)
        if node.right == None:
            return 1 + self.minDepthHelper(node.left)
        return 1 + min(self.minDepthHelper(node.left), self.minDepthHelper(node.right))