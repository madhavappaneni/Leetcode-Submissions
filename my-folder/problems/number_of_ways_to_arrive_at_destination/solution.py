class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v, time in roads:
            adjList[u].append((v, time))
            adjList[v].append((u, time))

        min_heap = [(0, 0)]
        distances, count = [float('inf')] * n, [0] * n
        distances[0], count[0] = 0, 1

        while min_heap:
            (min_dist, idx) = heappop(min_heap)
            if min_dist > distances[idx]: continue
            if idx == n-1: return count[idx] % (10**9 + 7)
            for nei, time in adjList[idx]:
                candidate = min_dist + time
                if candidate == distances[nei]:
                    count[nei] += count[idx]

                elif candidate < distances[nei]:
                    distances[nei] = candidate
                    heappush(min_heap, (time + min_dist, nei))
                    count[nei] = count[idx]
        return None