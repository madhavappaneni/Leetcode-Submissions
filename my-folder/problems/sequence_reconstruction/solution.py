class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indeg = Counter({n: 0 for n in nums})
        queue = deque([])

        for sequence in sequences:
            for i, j in zip(sequence, sequence[1:]):
                adjList[i].append(j)
                indeg[j] += 1
        
        queue.extend([i for i in indeg if indeg[i] == 0])

        res = []
        while queue:
            if len(queue) > 1:
                return False
            
            p = queue.pop()
            res.append(p)
            
            for nei in adjList[p]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)
            
        return nums == res