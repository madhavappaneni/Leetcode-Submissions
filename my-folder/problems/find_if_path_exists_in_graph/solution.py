class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        queue = collections.deque([source])
        visited = set()
        visited.add(source)

        while queue:
            currNode = queue.popleft()

            if currNode == destination:
                return True
            
            
            for nei in adjList[currNode]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        
        return False