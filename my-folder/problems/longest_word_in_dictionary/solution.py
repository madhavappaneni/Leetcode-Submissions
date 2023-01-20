class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.edges = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.edges:
                curr.edges[char] = TrieNode(char)
            curr = curr.edges[char]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.edges:
                return False
            curr = curr.edges[char]
        return curr.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        count = 0
        for char in prefix:
            if char not in curr.edges:
                break
            if curr.isEnd:
                count += 1
            curr = curr.edges[char]
        return count

class Solution:
    def longestWord(self, words: List[str]) -> str:
        maxScore = float('-inf')
        out = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        for word in words:
            score = trie.startsWith(word)
            # print(word, len(word), score)
            if score == len(word) - 1:
                if score > maxScore:
                    out = [word]
                    maxScore = score
                elif score == maxScore:
                    out.append(word)
        # print(sorted(out))
        return sorted(out)[0] if len(out) > 0 else ""
            

