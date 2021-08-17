class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        perm = [0] * (high)
        for i in range(len(s)):
            item = s[i]
            if item == "D":
                perm[i] = high
                high -= 1
            if item == "I":
                perm[i] = low
                low += 1
        return perm + [low]