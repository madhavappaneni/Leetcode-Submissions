# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxLevel = -1
        self.leftMostValue = None

        def dfs(node, currLevel):
            if node:
                if currLevel > self.maxLevel:
                    self.maxLevel = currLevel
                    self.leftMostValue = node.val
                if node.left:
                    dfs(node.left, currLevel + 1)
                if node.right:
                    dfs(node.right, currLevel + 1)
                return
        dfs(root, 0)
        return self.leftMostValue