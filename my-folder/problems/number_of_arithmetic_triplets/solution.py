class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        s = set(nums)
        for i in nums:
            if i + diff in s and i + 2 * diff in s:
                count += 1
        return count
        # return sum([1 if (i + diff) in nums and (i + 2 * diff) in nums else 0 for i in nums])