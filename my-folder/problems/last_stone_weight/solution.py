class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_stones = [-1 * stone for stone in stones]
        heapq.heapify(max_stones)
        print(max_stones)
        while len(max_stones) > 1:
            m, n = -1 * heapq.heappop(max_stones), -1 * heapq.heappop(max_stones)
            if m != n:
                heapq.heappush(max_stones, n-m)
        
        return -1 * max_stones[0] if len(max_stones) == 1 else 0