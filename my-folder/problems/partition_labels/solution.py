class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endOccurance = defaultdict(int)
        for i,ch in enumerate(s):
            endOccurance[ch] = i
        out = []
        maxEndIdx = -1
        size = 0
        for i, ch in enumerate(s):
            endIdx = endOccurance[ch]
            size += 1
            maxEndIdx = max(endIdx, maxEndIdx)
            if i == maxEndIdx:
                out.append(size)
                size = 0
        return out
