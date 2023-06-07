class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue = deque([[0]])
        # seen = set()
        # seen.add(0)
        n = len(graph)
        res = []
        while queue:
            path = queue.popleft()

            if path[-1] == n - 1:
                res.append(path)

            queue.extend([path + [nei] for nei in graph[path[-1]]])
        return res