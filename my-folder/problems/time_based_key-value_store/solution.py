class TimeMap:

    def __init__(self):
        self.TimeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        low, high = 0, len(self.TimeMap[key])

        while low < high:
            mid = (low + high) >> 1

            if self.TimeMap[key][mid][0] <= timestamp:
                low = mid + 1
            else:
                high = mid

        # return self.TimeMap[key][low][1]
        return "" if high == 0 else self.TimeMap[key][high - 1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)