class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        visited = [False] * numCourses
        color = [False] * numCourses
        
        
        def dfs(node):
            if visited[node] == True:
                return False
            
            if graph[node] == []:
                return True
            visited[node] = True
            
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            graph[node] = []
            visited[node] = False
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
