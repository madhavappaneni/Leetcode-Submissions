class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        # h = [(-1 * value, key) for key, value in c.items()]
        # heapq.heapify(h)
        # out = []
        # while k > 0:
        #     p = heapq.heappop(h)
        #     out.append(p[1])
        #     k -= 1
        # return out
        # TC - O(k.logN + N)

        h = []
        
        for key in c:
            heapq.heappush(h, (c[key], key))
            if len(h) > k:
                heappop(h)
        
        return [k for v, k in h]

        # Time complexity

