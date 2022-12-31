       
class Solution:
    # def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    #     g = collections.defaultdict(list)
    #     for edge in edges:
    #         g[edge[0]].append(edge[1])
    #         g[edge[1]].append(edge[0])
    #     visited = set()
    #     def helper(curr):
    #         if curr in visited:
    #             return
    #         elif curr == destination:
    #             return True
    #         else:
    #             visited.add(curr)
    #             for nei in g[curr]:
    #                 if helper(nei):
    #                     return True
    #         return False
    #     return helper(source)
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = collections.defaultdict(list)
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        seen = [False] * n
        seen[source] = True
        deq = collections.deque([source])
        while deq:
            elem = deq.popleft()
            if elem == destination:
                return True
            for nei in g[elem]:
                if not seen[nei]:
                    seen[nei] = True
                    deq.append(nei)
        return False
        

        