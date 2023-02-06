class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxVal = 0
        currVal = 0
        for g in gain:
            currVal += g
            maxVal = max(maxVal, currVal)
    
        return maxVal