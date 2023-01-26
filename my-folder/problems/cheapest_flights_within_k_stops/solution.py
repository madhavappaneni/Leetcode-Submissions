class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        costs = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append(v)
            costs[(u,v)] = cost
        
        @lru_cache(None)
        def solve(node, k):
            if node == dst:
                return 0
            if k == 0:
                if dst in graph[node]:
                    return costs[(node, dst)]
                else:
                    return -1
            minAns = float('inf')
            for nei in graph[node]:
                neiCost = solve(nei, k-1) 
                if neiCost != -1:
                    minAns = min(minAns, neiCost + costs[(node, nei)])
            return minAns if minAns != float('inf') else -1
        return solve(src, k)