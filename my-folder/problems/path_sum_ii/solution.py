# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        out = []
        def dfs(node, currPath, currSum):
            if not node:
                return
            currPath = currPath + [node.val]
            currSum += node.val

            if node.left == None and node.right == None and currSum == targetSum:
                out.append(currPath)
            
            dfs(node.left, currPath, currSum)
            dfs(node.right, currPath, currSum)
            return
        dfs(root, [], 0)
        return out
