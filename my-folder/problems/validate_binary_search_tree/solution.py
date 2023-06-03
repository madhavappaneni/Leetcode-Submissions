# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, minValue, maxValue):
            if not node:
                return True
            
            return minValue < node.val < maxValue and helper(node.left, minValue, node.val) and helper(node.right, node.val, maxValue)
        
    
        return helper(root, float('-inf'), float('inf'))