class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len(hand) % groupSize != 0:
        #     return False
            
        # count = Counter(hand)
        # minHeap = list(count.keys())
        # heapify(minHeap)

        # while minHeap:
        #     first = minHeap[0]

        #     for i in range(first, first + groupSize):
        #         if i not in count:
        #             return False
                
        #         count[i] -= 1

        #         if count[i] == 0:
        #             heappop(minHeap)
        # return True

        hand.sort()

        while hand:
            try:
                first = hand[0]
                for i in range(groupSize):
                    hand.remove(first + i)
            except:
                return False
        return True