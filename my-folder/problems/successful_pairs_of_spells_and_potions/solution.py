class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        N = len(potions)
        count = [0] * (len(spells))

        for idx,spell in enumerate(spells):
            targetElem = math.ceil(success/spell)
            insertIdx = bisect.bisect_left(potions, targetElem)
            count[idx] = (N - insertIdx)
        
        return count