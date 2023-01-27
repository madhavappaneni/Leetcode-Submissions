# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        h = collections.defaultdict(int)
        out = set()

        def postorder(node):
            if not node:
                return ''
            left = postorder(node.left)
            right = postorder(node.right)
            ans = '(' + left + ')' + str(node.val) + '(' + right + ')'
            h[ans] += 1
            if h[ans] == 2:
                out.add(node)
            return ans
        postorder(root)
        return list(out)

       