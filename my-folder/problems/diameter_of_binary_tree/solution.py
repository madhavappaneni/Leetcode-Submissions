# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node): # diameter, height
            if not node:
                return 0, -1
            ld, lh = dfs(node.left)
            rd, rh = dfs(node.right)
            height = max(lh, rh) + 1
            diameter = max(ld, rd, lh + rh + 2)
            return diameter, height

        diameter, _ = dfs(root)

        return diameter
        
