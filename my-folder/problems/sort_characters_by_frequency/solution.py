class Solution:
    def frequencySort(self, s: str) -> str:
        out = ""
        for i in sorted(Counter(s).items(), key=lambda x: -x[1]):
            out += i[0] * i[1]
        return out