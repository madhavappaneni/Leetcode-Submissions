class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = collections.defaultdict(list)

        for src, dest in edges:
            if src == destination:
                return False
            g[src].append(dest)

        status = [-1] * n

        GREY = 1
        BLACK = 0

        def dfs(node):
            if status[node] != -1:
                return status[node] == BLACK

            if len(g[node]) == 0:
                return node == destination
            status[node] = GREY

            for nei in g[node]:
                if not dfs(nei):
                    return False
            status[node] = BLACK
            return True

        return dfs(source)

