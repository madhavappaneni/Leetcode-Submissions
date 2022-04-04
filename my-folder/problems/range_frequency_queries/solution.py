class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.h = {}
        for i, val in enumerate(arr):
            val = str(val)
            if val in self.h:
                self.h[val].append(i) 
            else:
                self.h[val] = [i]
        # print(self.h)
        
    def query(self, left: int, right: int, value: int) -> int:
        if str(value) not in self.h:
            return 0
        i = bisect.bisect(self.h[str(value)], left - 1)
        j = bisect.bisect(self.h[str(value)], right)
        return j - i
    
    
# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)