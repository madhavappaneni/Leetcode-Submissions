class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashS = {}
        hashT = {}
        
        for i in s:
            if i not in hashS:
                hashS[i] = 1
            else:
                hashS[i] += 1
        
        for i in t:
            if i not in hashT:
                hashT[i] = 1
            else:
                hashT[i] += 1
        count = 0
        for elem in hashS:
            if elem not in hashT:
                count += hashS[elem]
            elif hashS[elem] != hashT[elem]:
                count += abs(hashS[elem] - hashT[elem])
        for elem in hashT:
            if elem not in hashS:
                count += hashT[elem]
            # elif hashS[elem] != hashT[elem]:
            #     count += abs(hashS[elem] - hashT[elem])
        print(hashS)
        print(hashT)
        return count
        
        