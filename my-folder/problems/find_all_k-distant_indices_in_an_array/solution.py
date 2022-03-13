class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = [i for i, x in enumerate(nums) if x == key]
        # print(indices)
        arr = set()
        for i, num in enumerate(nums):
            for index in indices:
                if abs(i - index) <= k:
                    # print(i, index)
                    arr.add(i)
                    break
        return sorted(list(arr))