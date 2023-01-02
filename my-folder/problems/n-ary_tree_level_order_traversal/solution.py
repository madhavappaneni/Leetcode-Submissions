"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = collections.deque()
        if root is None:
            return root
        queue.append(root)
        out = []
        while queue:
            levelOut = []
            for i in range(len(queue)):
                nei = queue.popleft()
                levelOut.append(nei.val)
                for child in nei.children:
                    queue.append(child)
            out.append(levelOut)
        return out
                