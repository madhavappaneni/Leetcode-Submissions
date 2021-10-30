class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter = 0
        for i in range(200):
            for j in range(len(strs)):
                try:
                    if(strs[j][i] != strs[0][i]):
                        return strs[0][:counter]
                except IndexError:
                    return strs[0][:counter]
            counter = counter + 1