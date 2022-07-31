class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        while len(hand) != 0:
            temp = hand[0]
            for i in range(temp, temp + groupSize):
                if i in hand:
                    hand.pop(hand.index(i))
                else:
                    # print(i, hand)
                    return False
        return True