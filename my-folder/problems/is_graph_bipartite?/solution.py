class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False] * len(graph)
        from collections import deque
        nodeColor = {}

        def bfsHelper(node):
            visited[node] = True
            deq = deque()
            deq.append([node, 'R'])
            colorMap = {
                'R': 'G',
                'G': 'R'
            }
            nodeColor[node] = 'R'

            while deq:
                element, color = deq.popleft()
                for neighbor in graph[element]:
                    if not visited[neighbor]:
                        deq.append([neighbor, colorMap[color]])
                        nodeColor[neighbor] = colorMap[color]
                        visited[neighbor] = True
                    else:
                        if nodeColor[neighbor] != colorMap[color]:
                            return False
            return True

        res = True
        for i in range(len(graph)):
            if not visited[i]:
                bfsRes = bfsHelper(i)
                res = res and bfsRes
        return res