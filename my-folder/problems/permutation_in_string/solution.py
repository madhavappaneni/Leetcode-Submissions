class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = Counter(s1)
        countS2 = Counter()
        s1Keys = list(countS1.keys())

        def checkSimilarity():

            for key in s1Keys:
                if countS2[key] != countS1[key]:
                    return False
            return True
        
        for i in range(len(s2)):
            countS2[s2[i]] += 1
            if i - len(s1) >= 0:
                countS2[s2[i - len(s1)]] -= 1
            # print(countS2)
            if checkSimilarity():
                return True
        return False
            
        
    