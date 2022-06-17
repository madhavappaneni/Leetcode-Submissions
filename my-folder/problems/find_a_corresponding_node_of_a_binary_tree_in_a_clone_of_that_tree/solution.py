# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(original, cloned):
            if original == None:
                return None
            if original == target:
                self.ans = cloned
                return 
            helper(original.left, cloned.left)
            helper(original.right, cloned.right)
        helper(original, cloned)
        return self.ans
   