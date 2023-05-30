# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.count = 0
        # self.ans = None
        # def helper(node):
        #     if not node:
        #         return
        #     helper(node.left)
        #     self.count += 1
        #     if self.count == k:
        #         self.ans = node.val
        #     helper(node.right)
        # helper(root)
        # return self.ans
        
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


