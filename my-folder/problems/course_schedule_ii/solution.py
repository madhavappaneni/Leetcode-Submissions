class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        graph = collections.defaultdict(list)
        
        for prereq in prerequisites:
            indegree[prereq[0]] += 1
            graph[prereq[1]].append(prereq[0])
        # print(indegree)
        deq = collections.deque()
        
        for idx, indeg in enumerate(indegree):
            if indeg == 0:
                deq.append(idx)
        visited = set() 
        out = []
        while deq:
            p = deq.pop()
            # print(p, visited, deq, indegree)
            if p not in visited:
                out.append(p)
                # add p to visited
                visited.add(p)
                # decrease indegree of neighbors of p by 1
                for nei in graph[p]:
                    indegree[nei] -= 1
                    # if indegree of the node becomes zero, add it to the deque
                    if indegree[nei] == 0:
                        deq.append(nei)
            
        return out if len(visited) == numCourses else []
        
        
        