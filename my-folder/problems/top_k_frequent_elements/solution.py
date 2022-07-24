class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print(count)
        sortedCount = sorted(count.items(), key = lambda x : -1 * x[1])
        print(sortedCount)
        out = []
        for i in range(k):
            out.append(sortedCount[i][0])
        return out
        