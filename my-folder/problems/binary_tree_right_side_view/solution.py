# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def helper(node, level):
            if not node:
                return
            if len(out) == level:
                out.append(node.val)
            helper(node.right, level + 1)
            helper(node.left, level + 1)
        
        helper(root, 0)
        return out