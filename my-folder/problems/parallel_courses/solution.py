class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adjList = defaultdict(list)
        indeg = defaultdict(int)

        for prevCourse, nextCourse in relations:
            adjList[prevCourse].append(nextCourse)
            indeg[nextCourse] += 1
        
        queue = deque([])
        
        for i in range(1, n + 1):
            if indeg[i] == 0:
                queue.append(i)
            
        if len(queue) == 0:
            return -1
        
        numSemesters = 0
        numCoursesCompleted = 0

        while queue:
            numSemesters += 1
            queueLen = len(queue)

            for i in range(queueLen):
                p = queue.popleft()
                numCoursesCompleted += 1
                for nei in adjList[p]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        queue.append(nei)
        
        return numSemesters if numCoursesCompleted == n else -1


