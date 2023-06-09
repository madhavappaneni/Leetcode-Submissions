class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adjList = defaultdict(set)
        indeg = Counter({c : 0 for word in words for c in word})

        for firstWord, secondWord in zip(words, words[1:]):
            for c, d in zip(firstWord, secondWord):
                if c != d:
                    if d not in adjList[c]:
                        adjList[c].add(d)
                        indeg[d] += 1
                    break
            else:
                if len(firstWord) > len(secondWord): return ""
        
        order = []
        queue = deque([c for c in indeg if indeg[c] == 0])
        while queue:
            p = queue.popleft()
            order.append(p)
            for nei in adjList[p]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)
        
        if len(order) < len(indeg):
            return ""

        return ''.join(order)