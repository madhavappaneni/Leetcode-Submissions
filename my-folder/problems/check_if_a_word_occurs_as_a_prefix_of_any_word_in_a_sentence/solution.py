class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sent_split = sentence.split(' ')
        for i, val in enumerate((sent_split)):
            if searchWord == val[0: len(searchWord)]:
                return i + 1
        return -1 