# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return root
        d = deque()
        d.append(root)
        res = []
        while d:
            l = len(d)
            for i in range(l):
                e = d.popleft()
                if i == l - 1:
                    res.append(e.val)
                if e.left:
                    d.append(e.left)
                if e.right:
                    d.append(e.right)
        return res
                    