


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.maxAns = 0
        graph = defaultdict(list)

        for idx, parent in enumerate(parent):
            if parent != -1:
                graph[parent].append(idx)

        def dfs(node):
            ans, left, right = 0, 0, 0
            ansValues = []
            for nei in graph[node]:
                if s[nei] != s[node]:
                    possAns = dfs(nei)
                    ansValues.append(possAns)
                else:
                    dfs(nei)
            heapify(ansValues)
            maxAns = sum(nlargest(2, ansValues)) + 1 if len(ansValues) != 0 else 1
            print(node, maxAns, ansValues, nlargest(2, ansValues))
            self.maxAns = max(self.maxAns, maxAns)
            return nlargest(1, ansValues)[0] + 1 if ansValues else 1
        
        dfs(0)
        return self.maxAns

        

        
