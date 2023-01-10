# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 0))
        maxWid = 0
        while queue:
            queuelen = len(queue)
            _, level_head_index = queue[0]
            for _ in range(queuelen):
                node, score = queue.popleft()
                print(node.val, score)
                if node.left: queue.append((node.left, 2 * score))
                if node.right: queue.append((node.right, 2 * score + 1))
            maxWid = max(maxWid, score - level_head_index + 1)
        return maxWid
        