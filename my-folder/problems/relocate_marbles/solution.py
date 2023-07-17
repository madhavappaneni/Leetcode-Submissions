class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        
        s = set(nums)
        
        for fr, to in zip(moveFrom, moveTo):
            s.remove(fr)
            s.add(to)
        
        return sorted(s)
        
        
        