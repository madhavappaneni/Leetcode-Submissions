class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = collections.defaultdict(list)
        count = collections.defaultdict(int)
        for ticket in tickets:
            g[ticket[0]].append(ticket[1])
        
        for origin, destinations in g.items():
            destinations.sort()
            print(origin, destinations)
            count[origin] = [False] * len(destinations)
        out = []
        
        def helper(curr, route):
            if len(route) == len(tickets) + 1:
                out.append(route)
                return True
            for i, destination in enumerate(g[curr]):
                if not count[curr][i]:
                    count[curr][i] = True
                    ret = helper(destination, route+[destination])
                    count[curr][i] = False
                    if ret:
                        return True
            return False
        helper('JFK', ['JFK'])
        return out[0]
                
                