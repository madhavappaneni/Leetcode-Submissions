# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # self.prev = float('-inf')
        # def inorder(node):
        #     global prev

        #     if not node:
        #         return True
        #     if not inorder(node.left):
        #         return False
        #     # print(prev, node.val)
        #     if self.prev >= node.val:
        #         return False
        #     self.prev = node.val
        #     return inorder(node.right)
        
        # return inorder(root)

        def helper(node, minValue, maxValue):
            if not node:
                return True
            elif node.val <= minValue or node.val >= maxValue:
                return False
            return helper(node.right, node.val, maxValue) and helper(node.left, minValue, node.val)
        return helper(root, float('-inf'), float('inf'))