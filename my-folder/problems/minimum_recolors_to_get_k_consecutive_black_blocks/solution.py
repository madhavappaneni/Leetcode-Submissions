class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blackCount = 0
        whiteCount = 0
        minAns = float("inf")
        
        for i in range(k):
            if blocks[i] == "B":
                blackCount += 1
            else:
                whiteCount += 1
                
        minAns = min(minAns, whiteCount)
        # print(whiteCount)
    
        for i in range(k, len(blocks)):
            # print(i, k, blocks[i-k])
            if blocks[i - k] == "B":
                blackCount -= 1
            else:
                whiteCount -= 1
            
            if blocks[i] == "B":
                blackCount += 1
            else:
                whiteCount += 1
            
            minAns = min(minAns, whiteCount)
            # print(blocks[i], whiteCount)
        return minAns