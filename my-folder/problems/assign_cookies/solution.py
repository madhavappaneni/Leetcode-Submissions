class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        i = 0
        g.sort()
        s.sort()
        lenS = len(s)
        for elem in g:
            while i < lenS:
                if elem <= s[i]:
                    count += 1 
                    i = i + 1
                    break
                else:
                    i = i + 1
        return count