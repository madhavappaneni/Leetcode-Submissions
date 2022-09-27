# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            h = collections.defaultdict(list)
            maxColumn = minColumn = 0
            if not root:
                return None
            deq = collections.deque()
            deq.append((root, 0))
            while deq:
                p, col = deq.pop()
                if p is not None:
                    h[col].append(p.val)
                    maxColumn = max(maxColumn, col)
                    minColumn = min(minColumn, col)
                    deq.appendleft((p.left, col - 1))
                    deq.appendleft((p.right, col + 1))
                    
            return ([h[x] for x in range(minColumn, maxColumn + 1)])
        return bfs(root)