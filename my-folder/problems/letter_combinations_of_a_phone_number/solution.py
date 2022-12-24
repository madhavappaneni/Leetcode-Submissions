class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        out = []
        def helper(currIdx, prefix):
            if currIdx < 0 or currIdx > 9:
                return
            elif currIdx == len(digits):
                if prefix != "":
                    out.append(prefix)
            else:
                for letter in letters[digits[currIdx]]:
                    helper(currIdx + 1, prefix + letter)
        helper(0, "")
        return out