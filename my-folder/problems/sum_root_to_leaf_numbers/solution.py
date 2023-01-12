# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        if not root:
            return 0
        
        def dfs(node, currValue):
            if not node:
                return 
            currValue = currValue * 10 + (node.val)
            if not node.left and not node.right:
                self.sum += currValue
            dfs(node.left, currValue)
            dfs(node.right, currValue)
        
        dfs(root, 0)

        return self.sum

            