class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        out = []
        for elem in people:
            out.insert(elem[1], elem)
        return out