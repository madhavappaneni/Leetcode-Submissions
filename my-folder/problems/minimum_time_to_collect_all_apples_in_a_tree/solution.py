class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = set()
        self.count = 0
        def dfs(node):
            ret = False
            if hasApple[node]:
                ret = True
            visited.add(node)

            for nei in graph[node]:
                if nei in visited:
                    continue
                if dfs(nei):
                    self.count += 2
                    ret = True
            return ret
        dfs(0)
        return self.count

            
