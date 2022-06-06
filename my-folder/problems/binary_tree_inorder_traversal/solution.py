# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        res = self.inorderTraversalHelper(root, res)
        return res

    def inorderTraversalHelper(self, root, res):
        if root == None:
            return None
        self.inorderTraversalHelper(root.left, res)
        res.append(root.val)
        self.inorderTraversalHelper(root.right, res)
        return res