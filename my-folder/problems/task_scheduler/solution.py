class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque([])
        c = Counter(tasks)
        heap = [-value for value in c.values()]
        heapify(heap)

        time = 0

        while heap or queue:
            time += 1

            if not heap:
                time = queue[0][1]
            else:
                cnt = 1 + heappop(heap)
                if cnt:
                    queue.append([cnt, time + n])
                
            if queue and queue[0][1] == time:
                heappush(heap, queue.popleft()[0])
                

        return time
        
        















    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     c = Counter(tasks)
    #     frequencies = list(c.values())
    #     frequencies.sort()
    #     f_max = frequencies.pop()
    #     idleTime = (f_max - 1) * n

    #     while frequencies and idleTime > 0:
    #         idleTime -= min(f_max - 1, frequencies.pop())
    #         # if freq.pop == fmax, take fmax - 1, else take freq.pop. 
    #         # A _ _ A _ _ A _ _ A
    #         # Consider B frequency is 4, it will take only 3 idle spaces.
    #         # A B _ A B _ A B _ A B - took only 3 of idle spaces
    #         # If B's frequency is < 4, it will take f idle spaces. 
    #     idleTime = max(idleTime, 0)

    #     return len(tasks) + idleTime
