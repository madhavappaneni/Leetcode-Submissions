class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indeg = defaultdict(int)
        queue = deque([])

        for u, v in prerequisites:
            adjList[u].append(v)
            indeg[v] += 1
        
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)
        
        nodesVisited = 0

        while queue:
            p = queue.popleft()
            nodesVisited += 1    
            for nei in adjList[p]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)
        
        return nodesVisited == numCourses
                

