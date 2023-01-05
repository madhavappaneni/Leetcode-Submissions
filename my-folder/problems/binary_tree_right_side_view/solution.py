# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        out = []

        def dfs(node, level):
            if not node:
                return
            if level == len(out):
                out.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, level = 0)
        return out