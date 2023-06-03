class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums

            pivot = int(len(nums) / 2)

            left = mergeSort(nums[:pivot])
            right = mergeSort(nums[pivot:])

            return merge(left, right)
        
        def merge(left, right):
            l, r = 0, 0
            out = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    out.append(left[l])
                    l += 1
                else:
                    out.append(right[r])
                    r += 1
            
            out.extend(left[l:])
            out.extend(right[r:])
            
            return out
        
        return mergeSort(nums)