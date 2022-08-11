class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [x % 60 for x in time]
        c = defaultdict(int)
        count = 0
        for t in time:
            complement = (60 - t) % 60
            # print(t, complement, count)
            if complement in c:
                count += c[complement]
            c[t] += 1
            # print(c)
        return count 