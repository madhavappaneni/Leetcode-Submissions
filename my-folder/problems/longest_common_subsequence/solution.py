class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        opt = [[0 for _ in range(len(text2) + 1)] for _ in range(1 + 1)]
        
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i == 0 or j == 0:
                    opt[i % 2][j] = 0
                    continue
                if text1[i-1] == text2[j-1]:
                    opt[i%2][j] = opt[(i-1)%2][j-1] + 1
                else:
                    opt[i%2][j] = max(opt[(i-1)%2][j], opt[i%2][j-1])
                
        return opt[len(text1) % 2][len(text2)]