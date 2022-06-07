# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traversal(root, [])
    
    def traversal(self, root, res):
        if root == None:
            return None
        res.append(root.val)
        self.traversal(root.left, res)
        self.traversal(root.right, res)
        return res