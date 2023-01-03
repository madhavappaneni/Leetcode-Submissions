class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for t in times:
            [src, dest, time] = t
            graph[src].append((time, dest)) #cost, time
            
        pq = [] 
        pq.append((0, k)) #cost, time
        heapq.heapify(pq)
        visited = set()
        destinationCosts = [float('inf') for _ in range(n + 1)] 
        destinationCosts[0] = 0
        destinationCosts[k] = 0
        
        out = 0
        while pq:
            currCost, currNode = heapq.heappop(pq)
            if currNode in visited:
                continue
            out = max(currCost, out)
            visited.add(currNode)
            for neiCost, neiNode in graph[currNode]:
                if neiNode not in visited and neiCost + currCost < destinationCosts[neiNode]:
                    destinationCosts[neiNode] = neiCost + currCost
                    heapq.heappush(pq, (destinationCosts[neiNode], neiNode))
            
        return out if len(visited) == n else -1