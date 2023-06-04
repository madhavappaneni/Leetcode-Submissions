class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []

        def helper(currIdx, currPrefix):
            if len(currPrefix) == k:
                out.append(currPrefix.copy())
                return
            
            need = k - len(currPrefix)
            remain = n - currIdx + 1
            available = remain - need
            
            for i in range(currIdx + 1, currIdx + available + 1):
                currPrefix.append(i)
                helper(i, currPrefix)
                currPrefix.pop()
            return
        
        helper(0, [])
    
        return out
