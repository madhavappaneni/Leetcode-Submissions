class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for i in range(1, numRows):
            prevRow = ans[-1]
            currRow = [1]
            for j in range(0, len(prevRow) - 1):
                currRow.append(prevRow[j] + prevRow[j+1])
            currRow.append(1)
            ans.append(currRow)
        return ans
                
