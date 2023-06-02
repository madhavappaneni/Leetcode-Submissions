class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        freeServerHeap = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(freeServerHeap)
        
        busyServerHeap = []
        ans = []
        for time, task in enumerate(tasks):
            while len(busyServerHeap) > 0 and busyServerHeap[0][0] == time:
                freeServer = heapq.heappop(busyServerHeap)
                heapq.heappush(freeServerHeap, freeServer[1])

            if len(freeServerHeap) == 0:
                finishTime, currServer = heappop(busyServerHeap)
                heappush(busyServerHeap, (task + finishTime, currServer))
                ans.append(currServer[1])
            else:
                currServer = heapq.heappop(freeServerHeap)
                ans.append(currServer[1])
                heapq.heappush(busyServerHeap, (time + tasks[time], currServer))
        return ans