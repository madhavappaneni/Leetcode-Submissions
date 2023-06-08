class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def dfs(node):
            print(node)
            if node in visited:
                return
            visited.add(node)

            for nei in adjList[node]:
                dfs(nei)
            return

        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count