class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        totalSum = sum(nums)

        if totalSum % k != 0:
            return False

        targetSum = totalSum // k

        taken = set()
        nums.sort(reverse=True)


        def backtrack(index, count, currSum):
            if count == k:
                return True
            
            if currSum == targetSum:
                return backtrack(0, count + 1, 0)
            
            for p in range(index, n):
                if p > 0 and (p - 1) not in taken and nums[p] == nums[p - 1]:
                    continue

                if p in taken or currSum + nums[p] > targetSum:
                    continue

                taken.add(p)

                if backtrack(p + 1, count, currSum + nums[p]):
                    return True
                
                taken.remove(p)
        
            return False
        

        return backtrack(0, 0, 0)