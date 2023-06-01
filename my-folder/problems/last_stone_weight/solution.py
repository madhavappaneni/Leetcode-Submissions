class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStones = [-1 * stone for stone in stones]
        heapq.heapify(maxStones)
        h = maxStones

        while h and len(h) >= 2:
            first, second = heapq.heappop(h), heapq.heappop(h)
            if first != second:
                heapq.heappush(h, first - second)
            
        return -1 * h[0] if h else 0