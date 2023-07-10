# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # def isSame(root1, root2):
        #     def getValue(node):
        #         if node:
        #             return node.val
        #         return None

        #     if not (root1 or root2):
        #         return True
        #     if not (root1 and root2):
        #         return False
        #     if root1.val == root2.val:
        #         if (getValue(root1.left) == getValue(root2.right) and getValue(root1.right) == getValue(root2.left)):
        #             return isSame(root1.right, root2.left) and isSame(root1.left, root2.right)
        #         elif (getValue(root1.left) == getValue(root2.left) and getValue(root1.right) == getValue(root2.right)):
        #             return isSame(root1.left, root2.left) and isSame(root1.right, root2.right)

        def isSame(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2 or root1.val != root2.val:
                return False
            
            return (isSame(root1.left, root2.left) and isSame(root1.right, root2.right)) or (isSame(root1.right, root2.left) and isSame(root1.left, root2.right))
                
        return isSame(root1, root2)







