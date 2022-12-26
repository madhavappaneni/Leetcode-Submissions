class NumArray:

    def __init__(self, nums: List[int]):
        self.rangeSum = []
        currSum = 0
        for num in nums:
            currSum += num
            self.rangeSum.append(currSum)  
        print(self.rangeSum)      

    def sumRange(self, left: int, right: int) -> int:
        return self.rangeSum[right] - (self.rangeSum[left - 1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)