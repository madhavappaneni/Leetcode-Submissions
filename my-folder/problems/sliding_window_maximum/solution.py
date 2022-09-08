class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        out = []
        for i in range(k):
            
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
                
            deq.append(i)
        out.append(max(nums[:k]))
        for i in range(k, len(nums)):
            if deq and deq[0] == i - k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            out.append(nums[deq[0]])
        return out
    
    
    # bruteforce - O(nk)
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     out = []
    #     n = len(nums)
    #     for i in range(n - k + 1):
    #         out.append(max(nums[i: i + k]))
    #     return out