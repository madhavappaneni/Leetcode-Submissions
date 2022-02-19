class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}
        sSplit = s.split()
        lenPattern = len(pattern)
        lenS = len(sSplit)
        if lenPattern != lenS:
            return False
        for index, letter in enumerate(pattern):
            word = sSplit[index]
            if letter not in hashMap1:
                hashMap1[letter] = word
            if word not in hashMap2:
                hashMap2[word] = letter
            if hashMap1[letter] != word or hashMap2[word] != letter:
                return False
        return True
            