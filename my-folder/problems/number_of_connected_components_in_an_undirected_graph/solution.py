class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [0] * n
        
        for firstEdge, secondEdge in edges:
            graph[firstEdge].append(secondEdge)
            graph[secondEdge].append(firstEdge)
            
        def dfs(idx):
            for nei in graph[idx]:
                if visited[nei] == 0:
                    visited[nei] = 1
                    dfs(nei)
        # print(graph)
        count = 0
        for i in range(n):
            # print(visited)
            if visited[i] == 0 :
                count += 1
                visited[i] = 1
                dfs(i)
            
        return count