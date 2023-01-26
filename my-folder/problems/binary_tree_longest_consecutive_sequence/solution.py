# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxLen = float('-inf')

        def dfs(node, currLen, prev):
            if not node:
                return 0
            else:
                if node.val == prev + 1:
                    currLen += 1
                    self.maxLen = max(self.maxLen, currLen)
                else:
                    currLen = 1
                dfs(node.left, currLen, node.val)
                dfs(node.right, currLen, node.val)
                return currLen
        if not root:
            return 0
        dfs(root, 0, root.val - 1)
        return self.maxLen