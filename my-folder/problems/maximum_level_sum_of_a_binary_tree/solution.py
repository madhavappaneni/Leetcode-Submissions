# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        maxLevelSum = float('-inf')
        minLevel = -1
        currLevel = 0

        while queue:
            currLevel += 1
            queueLen = len(queue)
            levelSum = 0
            for i in range(queueLen):
                elem = queue.popleft()
                levelSum += elem.val
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
            if levelSum > maxLevelSum:
                maxLevelSum = levelSum
                minLevel = currLevel
        
        return minLevel