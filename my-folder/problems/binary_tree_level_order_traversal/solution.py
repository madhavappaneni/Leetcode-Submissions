# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        out = []
        while queue:
            level_out = []
            queue_len = len(queue)
            for i in range(queue_len):
                p = queue.popleft()
                level_out.append(p.val)
                if p.left: queue.append(p.left)
                if p.right: queue.append(p.right)
            out.append(level_out)
        return out