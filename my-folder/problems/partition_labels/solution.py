class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndexMap = {}
        for i, v in enumerate(s):
            lastIndexMap[v] = i
        size = 0
        out = []
        start, end = 0, 0
        for i, v in enumerate(s):
            size += 1
            if lastIndexMap[v] > end:
                end = lastIndexMap[v]
            if i == end:
                out.append(size)
                size = 0
        return (out)