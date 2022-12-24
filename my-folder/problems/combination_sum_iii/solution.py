class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        out = []
        def helper(target, currIndex, k, currArr):
            if target < 0 or k < 0:
                return
            elif target == 0 and k == 0:
                out.append(currArr.copy())
            else:
                for idx in range(currIndex, 10):
                    currArr.append(idx)
                    helper(target - idx, idx + 1, k - 1, currArr)
                    currArr.pop()
        helper(n, 1, k, [])
        return out
        
