# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = collections.defaultdict(list)
        def dfs(curr, currHeight):
            if not curr:
                return currHeight
            left = dfs(curr.left, currHeight)
            right = dfs(curr.right, currHeight)
            currHeight = max(left, right)
            h[currHeight].append(curr.val)
            return currHeight + 1
        dfs(root, 0)
        return h.values()