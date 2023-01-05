# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        queue = deque([root])
        out = []
        currDir = 1
        while queue:
            queueLen = len(queue)
            levelOut = deque()
            for i in range(queueLen):
                p = queue.popleft()
                if currDir == 1:
                    levelOut.append(p.val)
                else:
                    levelOut.appendleft(p.val)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
            out.append(levelOut)
            currDir *= -1
        return out