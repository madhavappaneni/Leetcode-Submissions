# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:        
        def dfs(root):
            if root.left == None and root.right == None:
                return False if root.val == 0 else True
            left = dfs(root.left)
            right = dfs(root.right)
            return (left and right) if root.val == 3 else (left or right)
        return dfs(root)