class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        pCopy = deepcopy(passengers)
        heapify(buses)
        heapify(passengers)
        print(sorted(buses))
        print(sorted(passengers))
        finalBatch = []
        bus = 0
        while len(buses) > 0:
            bus = heappop(buses)
            currCap = capacity
            finalBatch = []
            while len(passengers) > 0 and passengers[0] <= bus and currCap > 0:
                currCap -= 1
                finalBatch.append(heappop(passengers))
        print(finalBatch)
        ans = 0
        if len(finalBatch) < capacity:
            ans = bus
        else:            
            ans = finalBatch[-1]
        
        while ans in pCopy:
            ans -= 1
        
        return ans