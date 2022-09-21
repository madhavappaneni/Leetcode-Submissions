class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.h = collections.defaultdict(list)
        for i, val in enumerate(arr):
            self.h[val].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        i = bisect.bisect(self.h[value], left - 1)
        j = bisect.bisect(self.h[value], right)
        return j - i


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)