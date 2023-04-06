class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = collections.defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        seen = set()
        def dfs(node):
            if node in seen: return False
            if node == destination: return True
            seen.add(node)
            return any([dfs(nei) for nei in adjList[node]])
        
        return dfs(source)