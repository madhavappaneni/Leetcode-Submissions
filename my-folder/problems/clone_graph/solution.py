"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def dfs(node):
            if not node:
                return node
            if node in visited:
                return visited[node]
            currNode = Node(node.val, [])
            visited[node] = currNode
            if node.neighbors:
                currNode.neighbors = [dfs(nei) for nei in node.neighbors]
            return currNode
        return dfs(node)
        