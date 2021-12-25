# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        out = deque()
        deq = deque()
        deq.append(root)
        if not root:
            return []
        direction = 1
        while deq:
            count = len(deq)
            levelOut = deque()
            while count > 0:
                if direction == -1:
                    element = deq.popleft()
                    levelOut.appendleft(element.val)
                    if element.left:
                        deq.append(element.left)
                    if element.right:
                        deq.append(element.right)
                elif direction == 1:
                    element = deq.popleft()
                    levelOut.append(element.val)
                    if element.left:
                        deq.append(element.left)
                    if element.right:
                        deq.append(element.right)
                count -= 1
            direction *= -1
            out.append(levelOut)
        return list(out)