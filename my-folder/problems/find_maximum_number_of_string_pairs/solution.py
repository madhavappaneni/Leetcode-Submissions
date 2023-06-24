class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        dict = defaultdict(int)
        result = 0
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word in dict and dict[sorted_word] == 1:
                dict[sorted_word] = 0
                result += 1
            else:
                dict[sorted_word] += 1
        
        return result