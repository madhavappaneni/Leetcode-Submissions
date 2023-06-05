class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberToLetterMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        out = []

        def helper(start, prefix):
            if start == len(digits) and prefix:
                out.append(prefix)
            if start >= len(digits):
                return
            for i in numberToLetterMap[digits[start]]:
                helper(start + 1, prefix + i)
            
            return
        
        helper(0, "")

        return out
