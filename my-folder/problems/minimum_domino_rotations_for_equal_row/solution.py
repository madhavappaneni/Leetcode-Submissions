class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        
        countTops = defaultdict(int)
        countBottoms = defaultdict(int)
        same = 0

        for t,b in zip(tops, bottoms):
            if t == b:
                same += 1
            countTops[t] += 1
            countBottoms[b] += 1
        
        for i in range(1, 7):
            if countTops[i] + countBottoms[i] - same == len(tops):
                return len(tops) - max(countTops[i], countBottoms[i])
            
        return -1
