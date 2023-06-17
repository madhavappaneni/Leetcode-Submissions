class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        @lru_cache(maxsize = None)
        def helper(currIdx, currM, currN):
            if currIdx == len(strs):
                return 0
                
            taken = -1
            c = Counter(strs[currIdx])
            zerosCount, onesCount = c.get('0', 0), c.get('1', 0)

            if zerosCount <= currM and onesCount <= currN:
                taken = helper(currIdx + 1, currM - zerosCount, currN - onesCount) + 1
            skipped = helper(currIdx + 1, currM, currN)
            
            return max(taken, skipped)

        return helper(0, m, n)
