class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        i = 0
        j = 0
        cardMap = {}
        currMax = float("inf")
        found = False
        for (i, card) in enumerate(cards):
            if card not in cardMap:
                cardMap[card] = i
            else:
                currMax = min(i - cardMap[card] + 1, currMax)
                cardMap[card] = i
                found = True
        return currMax if found else -1
            