class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # frequencies of tasks of the same level
        frequencies = list(Counter(tasks).values())
        rounds = 0
        for f in frequencies:
            if f == 1:
                return -1
            rounds += math.ceil(f / 3)
        return rounds

