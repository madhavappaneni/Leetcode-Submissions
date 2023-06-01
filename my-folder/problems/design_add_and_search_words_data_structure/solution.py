class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for ch in word:
            if ch not in curr:
                curr[ch] = {} 
            curr = curr[ch]       
        curr['$'] = True

    def search(self, word: str) -> bool:
        curr = self.trie

        def helper(word, node):
            for idx, ch in enumerate(word):
                if ch not in node:
                    if ch == '.':
                        for elem in node:
                            if elem != '$' and helper(word[idx + 1: ], node[elem]):
                                return True
                    return False
                else:
                    node = node[ch]
            return '$' in node
        
        return helper(word, curr)
                        

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)