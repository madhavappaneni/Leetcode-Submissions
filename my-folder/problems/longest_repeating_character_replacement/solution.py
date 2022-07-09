class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = Counter()
        i, j = 0, 0
        maxAns = 0
        while i < len(s) and j < len(s):
            d[s[j]] += 1
            vals = d.values()
            maxAns = max(maxAns, d[s[j]])
            if j - i + 1 > maxAns + k:
                d[s[i]] -= 1
                i += 1

            j += 1
            # print(d, i, j, maxAns)
        return len(s) - i