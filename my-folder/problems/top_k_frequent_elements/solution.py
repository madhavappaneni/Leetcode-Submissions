class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [a[0] for a in Counter(nums).most_common(k)]