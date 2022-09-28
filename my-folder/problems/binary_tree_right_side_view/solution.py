# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        deq = collections.deque()
        deq.append(root)
        out = []
        while deq:
            l = len(deq)
            localOut = 0
            for i in range(l):
                poppedElem = deq.pop()
                if i == l - 1:
                    localOut = (poppedElem.val)
                if poppedElem.left: deq.appendleft(poppedElem.left)
                if poppedElem.right: deq.appendleft(poppedElem.right)
            out.append(localOut)
        return out