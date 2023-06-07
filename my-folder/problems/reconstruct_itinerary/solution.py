class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        tickets.sort()
        for src, dest in tickets:
            adjList[src].append(dest)
        
        path = ["JFK"]

        def dfs(node):
            if len(path) == len(tickets) + 1:
                return True
            if node not in adjList:
                return False

            temp = adjList[node].copy()
            
            for i, v in enumerate(temp):
                path.append(v)
                adjList[node].pop(i)

                if dfs(v):
                    return True

                path.pop()
                adjList[node].insert(i, v)

        dfs("JFK")
        return path