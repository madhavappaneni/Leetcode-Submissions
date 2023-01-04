class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        frequencies = list(c.values())
        frequencies.sort()
        f_max = frequencies.pop()
        idleTime = (f_max - 1) * n

        while frequencies and idleTime > 0:
            idleTime -= min(f_max - 1, frequencies.pop())
            # if freq.pop == fmax, take fmax - 1, else take freq.pop. 
            # A _ _ A _ _ A _ _ A
            # Consider B frequency is 4, it will take only 3 idle spaces.
            # A B _ A B _ A B _ A B - took only 3 of idle spaces
            # If B's frequency is < 4, it will take f idle spaces. 
        idleTime = max(idleTime, 0)

        return len(tasks) + idleTime
