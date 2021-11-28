class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lo, hi = 0, len(nums)-1
        answer = collections.deque()
        while lo <= hi:
            if abs(nums[lo]) < abs(nums[hi]):
                answer.appendleft(nums[hi] ** 2)
                hi = hi - 1
            else:
                answer.appendleft(nums[lo] ** 2)
                lo = lo + 1

        return list(answer) 