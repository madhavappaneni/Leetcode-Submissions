class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj_list = collections.defaultdict(list)

        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)
        
        seen = set()

        def dfs(node):
            if node in seen:
                return 
            seen.add(node)
            for nei in adj_list[node]:
                dfs(nei)

        dfs(0)

        return len(seen) == n