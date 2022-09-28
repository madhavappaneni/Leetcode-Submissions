# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True
        prev = float('-inf')
        def dfs(root):
            nonlocal isValid, prev
            if not root:
                return None
            dfs(root.left)
            # print(root.val, prev, root.val < prev, isValid)
            if root.val <= prev:
                isValid = False 
            prev = (root.val)
            dfs(root.right)
        dfs(root)
        return isValid