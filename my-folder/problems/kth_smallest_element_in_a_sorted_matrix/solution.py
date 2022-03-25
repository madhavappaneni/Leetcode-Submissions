class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        for row in matrix:
            for ele in row:
                heapq.heappush(h, -ele)
                if len(h) > k:
                    heapq.heappop(h)
        return -h[0]
