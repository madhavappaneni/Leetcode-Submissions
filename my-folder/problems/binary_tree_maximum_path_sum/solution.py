# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')

        def helper(node):
            if node:
                left = helper(node.left)
                right = helper(node.right)
                localMax = node.val + (left if left > 0 else 0) + (right if right > 0 else 0)
                self.maxPath = max(self.maxPath, localMax)
                # print(node.val, node.val + (max(left, right) if left > 0 and right > 0 else 0))
                return node.val + (max(left, right) if left > 0 or right > 0 else 0)
            else:
                # print(node, 0)
                return 0
        
        helper(root)
        return self.maxPath
            