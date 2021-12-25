# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        averages = []
        deq = deque()
        deq.append(root)
        while deq:
            count = len(deq)
            levelSize = len(deq)
            sum = 0            
            while count > 0:
                element = deq.popleft()
                sum += element.val
                if element.left:
                    deq.append(element.left)
                if element.right:
                    deq.append(element.right)
                count -= 1
            averages.append(sum*1.0/levelSize)
        return averages