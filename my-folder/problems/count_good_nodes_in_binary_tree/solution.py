# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        count = 0

        def helper(node, maxValue):
            nonlocal count
            if node.val >= maxValue:
                count += 1
            
            if node.left:
                helper(node.left, max(maxValue, node.val))
            
            if node.right:
                helper(node.right, max(maxValue, node.val))
        
        helper(root, root.val)
        
        return count