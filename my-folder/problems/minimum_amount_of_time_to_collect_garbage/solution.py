class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        sumT = 0
        rangeT = [0]
        for i in range(len(travel)):
            rangeT.append(rangeT[-1] + travel[i])
        gIdx, pIdx, mIdx = 0, 0, 0
        gCount, pCount, mCount = 0, 0, 0
        for idx, g in enumerate(garbage):
            c = Counter(g)
            if c.get('G', 0) > 0:
                gCount += c.get('G')
                gIdx = idx
            if c.get('P', 0) > 0:
                pCount += c.get('P')
                pIdx = idx
            if c.get('M', 0) > 0:
                mCount += c.get('M')
                mIdx = idx
        return (gCount + pCount + mCount) + (rangeT[gIdx] + rangeT[pIdx] + rangeT[mIdx])
    
            
