# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node:
                dfs(node.left)
                node.left = None
                self.curr.right = node
                self.curr = node
                dfs(node.right)
        ans = self.curr = TreeNode(None)
        dfs(root)
        return ans.right
        
            