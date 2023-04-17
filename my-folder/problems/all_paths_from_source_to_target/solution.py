class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        seen = set([0])
        deq = collections.deque([[0, [0]]])
        paths = []
        while deq:
            node, path = deq.pop()
            if node == len(graph) - 1:
                paths.append(path.copy())
            for nei in graph[node]:
                if nei not in seen:
                    deq.append([nei, path + [nei]])
        
        return paths
                    