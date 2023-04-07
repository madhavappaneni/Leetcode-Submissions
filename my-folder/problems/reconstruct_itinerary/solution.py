class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = collections.defaultdict(list)
        visitMap = collections.defaultdict(list)
        
        for source, destination in tickets:
            adjList[source].append(destination)

        for k, v in adjList.items():
            v.sort()
            visitMap[k] = [False] * len(v)
        self.path = ['JFK']

        def dfs(node, route):
            if len(route) == len(tickets) + 1:
                self.path = route                
                return True
            for i, nei in enumerate(adjList[node]):
                if not visitMap[node][i]:
                    visitMap[node][i] = True
                    ret = dfs(nei, route + [nei])
                    visitMap[node][i] = False
                    if ret:
                        return True
            return False

        
        dfs("JFK", ["JFK"])

        return self.path
        
