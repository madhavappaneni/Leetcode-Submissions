class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = [0] * n
        graph = collections.defaultdict(list)
        if n <= 2:
            return range(n)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        
        queue = collections.deque()
        # queue contains the leaves in one round
        
        for edge, deg in enumerate(degree):
            if deg == 1:
                queue.append(edge)
        
        remainingNodes = n
        # print(graph)
        while remainingNodes > 2:
            # print(queue)
            remainingNodes = remainingNodes - len(queue)
            queueLen = len(queue)
            for i in range(queueLen):
                elem = queue.popleft()
                for nei in graph[elem]:
                    # print(elem, nei)
                    degree[nei] -= 1
                    graph[nei].remove(elem)
                    if degree[nei] == 1:
                        queue.append(nei)
                    # print(degree, queue)
        return list(queue)
            