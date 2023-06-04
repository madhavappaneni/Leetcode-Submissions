class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        out = []

        def backtrack(currIdx, currPrefix, remSum):
            if remSum == 0 and len(currPrefix) == k:
                out.append(currPrefix[:])
            
            elif remSum < 0 or len(currPrefix) == k:
                return

            for i in range(currIdx + 1, 10):
                currPrefix.append(i)
                backtrack(i, currPrefix, remSum - i)
                currPrefix.pop()
            
            return
        
        backtrack(0, [], n)

        return out


