class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         visited = set()
#         out = []
#         destination = len(graph) - 1
#         def helper(curr, currPath):
#             if curr == destination:
#                 out.append(currPath)
#             else:
                
#                 visited.add(curr) 
#                 for nei in graph[curr]:
#                     helper(nei, currPath + [nei])
#         helper(0, [0])
#         return out
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        queue = collections.deque()
        destination = len(graph) - 1
        path = [0]
        queue.append(path)
        while queue:
            print(queue)
            path = queue.pop()
            node = path[-1]
            if node == destination:
                print(path)
                paths.append(path)
            for nei in graph[node]:
                temp_path = path.copy()
                temp_path.append(nei)
                queue.append(temp_path)

        return paths