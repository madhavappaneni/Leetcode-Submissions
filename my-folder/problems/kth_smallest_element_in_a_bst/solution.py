# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(curr):
            if not curr:
                return None
            dfs(curr.left)
            self.count += 1
            if self.count == k:
                self.ans = curr.val
            dfs(curr.right)
        self.ans = None
        self.count = 0
        dfs(root)
        return self.ans