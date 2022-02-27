class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        lenPref = len(pref)
        for word in words:
            if word[0:lenPref] == pref:
                count += 1
        return count