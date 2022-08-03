class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        out = [0] * 3
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            for i, v in enumerate(triplet):
                if v == target[i]:
                    out[i] = max(out[i], v)
        return out == target
                