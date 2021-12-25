# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        out = deque()
        deq = deque()
        deq.append(root)
        if not root:
            return []
        while deq:
            count = len(deq)
            levelOut = []
            while count > 0:
                element = deq.popleft()
                levelOut.append(element.val)
                if element.left:
                    deq.append(element.left)
                if element.right:
                    deq.append(element.right)
                count -= 1
            out.appendleft(levelOut)
        return list(out)