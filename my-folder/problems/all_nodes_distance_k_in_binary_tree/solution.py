# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        out = []
        def constructGraph(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                constructGraph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                constructGraph(node.right)
        constructGraph(root)
        
        visited = set()
        def getElemsInKDistance(curr, currK):
            if curr in visited:
                return
            visited.add(curr)
            if currK < 0 :
                return
            if currK == 0:
                out.append(curr)
            for nei in graph[curr]:
                getElemsInKDistance(nei, currK - 1)
        
        getElemsInKDistance(target.val, k)    
        return (out)