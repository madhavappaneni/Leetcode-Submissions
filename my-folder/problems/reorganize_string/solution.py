class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        h = [(-c[i], i) for i in c]
        heapify(h)
        out = []

        while len(h) >= 2:
            first, second = heappop(h), heappop(h)
            out.extend([first[1], second[1]])
            if first[0] < -1:
                heappush(h, (first[0] + 1, first[1]))
            if second[0] < -1:
                heappush(h, (second[0] + 1, second[1]))
        
        if h:
            p = heappop(h)
            if p[0] == -1:
                out.append(p[1])
            else:
                return ""
        
        return ''.join(out)
            
