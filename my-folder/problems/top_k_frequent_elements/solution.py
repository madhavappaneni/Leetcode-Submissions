class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        h = [(-1 * value, key) for key, value in c.items()]
        # print(h)
        heapq.heapify(h)
        out = []
        while k > 0:
            p = heapq.heappop(h)
            out.append(p[1])
            k -= 1
        return out
        # Time complexity of this solution is O(klogn), Whereas sorting and returning max k elements has a time complexity of O(N.logN)