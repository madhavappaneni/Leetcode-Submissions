class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        degree = [0] * (n + 1)
        graph = collections.defaultdict(list)
        
        for relation in relations:
            graph[relation[0]].append(relation[1])
            graph[relation[1]].append(relation[0])
            degree[relation[1]] += 1
        
        queue = collections.deque()
        
        for course, deg in enumerate(degree):
            if deg == 0 and course != 0:
                queue.append(course)
        if len(queue) == 0:
            return -1
        
        # print(queue)
        visited = set()
        semestersCount = 0
        while queue:
            semestersCount += 1
            queueLen = len(queue)
            for i in range(queueLen):
                elem = queue.popleft()
                if elem in visited:
                    continue
                visited.add(elem)
                for nei in graph[elem]:
                    degree[nei] -= 1
                    if degree[nei] == 0:
                        queue.append(nei)
        # print(visited)
        return semestersCount if len(visited) == n else -1
                      
                
        
        
            