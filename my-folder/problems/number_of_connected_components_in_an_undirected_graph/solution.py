class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adjList = collections.defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node):
            if node in seen:
                return 
            seen.add(node)
            for nei in adjList[node]:
                dfs(nei)
            
        count = 0

        for i in range(n):
            if i not in seen:
                dfs(i)
                count += 1

        return count