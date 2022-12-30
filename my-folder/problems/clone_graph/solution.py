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
        newNode = Node(None)
        def dfs(curr):
            if not curr:
                return
            if curr in visited:
                return visited[curr]
            newNode = Node(curr.val, [])
            for i in (curr.neighbors):
                visited[curr] = newNode
                newNode.neighbors = [dfs(nei) for nei in curr.neighbors]
            return newNode
        return dfs(node)