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
        def helper(node):
            if node == None:
                return None
            if node in visited:
                return visited[node]
            newNode = Node(node.val, [])
            visited[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(helper(nei))
            return newNode
        return helper(node)        