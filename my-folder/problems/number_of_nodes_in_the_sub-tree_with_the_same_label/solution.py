class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, prev):
            count = Counter()

            for nei in graph[node]:
                if nei != prev:
                    count += dfs(nei, node)
            
            count[labels[node]] += 1
            ans[node] = count[labels[node]]
            return count
        dfs(0, -1)
        return ans
        