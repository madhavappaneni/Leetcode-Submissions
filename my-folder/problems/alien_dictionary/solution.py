class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = collections.defaultdict(set)
        indegree = Counter({c : 0 for word in words for c in word})

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in graph[c]:
                        graph[c].add(d)
                        indegree[d] += 1
                    break
            else: 
                if len(second_word) < len(first_word): return ""

        zerodeg = deque([c for c in indegree if indegree[c] == 0])
        # print(graph)
        # print(indegree)
        # print(zerodeg)
        out = ""
        while zerodeg:
            elem = zerodeg.pop()
            out += (elem)
            for nei in graph[elem]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    zerodeg.append(nei)
        print(out)
        return out if len(indegree.items()) == len(out) else ""