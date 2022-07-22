class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberLetterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        out = []
        
        def dfs(idx, comb):
            if idx == len(digits):
                len(comb) > 0 and out.append(comb[:])
                return
            if idx > len(digits) or idx < 0:
                return
            for letter in numberLetterMap[digits[idx]]:
                dfs(idx + 1, comb + letter)
        dfs(0, "")
        return out