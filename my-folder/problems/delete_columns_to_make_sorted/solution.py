class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rowRanks = [0] * len(strs[0])
        deletedCols = set()

        for s in strs:
            for idx, char in enumerate(s):
                if ord(char) < rowRanks[idx]:
                    deletedCols.add(idx)
                rowRanks[idx] = ord(char)
        return len(deletedCols)