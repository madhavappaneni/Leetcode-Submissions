# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if not root:
            return count
        stack = collections.deque([(root, float('-inf'))])
        while stack:
            node, maxValue = stack.pop()
            if node.val >= maxValue:
                count += 1
            if node.left: stack.appendleft((node.left, max(node.val, maxValue)))
            if node.right: stack.appendleft((node.right, max(node.val, maxValue)))
        return count                
            