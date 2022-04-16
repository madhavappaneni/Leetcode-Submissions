class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dist = 111111
        for i in nums:
            i_dist = abs(i - 0)
            if i_dist < dist:
                dist = i_dist
        out = []
        for i in nums:
            i_dist = abs(i - 0)
            if i_dist == dist:
                out.append(i)
        return (sorted(out)[-1])
