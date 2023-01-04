class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        h = [(-1 * value, key) for key, value in c.items()]
        heapq.heapify(h)
        out = []
        while k > 0:
            p = heapq.heappop(h)
            out.append(p[1])
            k -= 1
        return out