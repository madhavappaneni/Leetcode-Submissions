class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = [[] for _ in range(n)]
        visited = [0] * n
        visited[0] = 1
        for r in restricted:
            visited[r] = -1
        # print(visited)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        count = 1
        def dfs(node):
            nonlocal count
            # print(node)
            for nei in graph[node]:
                if visited[nei] == 0:
                    count += 1
                    visited[nei] = 1
                    dfs(nei)

        dfs(0)
        return count