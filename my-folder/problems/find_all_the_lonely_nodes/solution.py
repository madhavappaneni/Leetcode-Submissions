# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(root, isAlone):
            if root == None: return
            isAlone == True and ans.append(root.val)
            isAlone = True if (root.left == None) ^ (root.right == None) else False
            helper(root.left, isAlone)
            helper(root.right, isAlone)
        helper(root, False)
        return ans
