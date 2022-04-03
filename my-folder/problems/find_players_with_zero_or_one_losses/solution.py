class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = {}
        for match in matches:
            if match[0] in players:
                players[match[0]]['w'] += 1
            else:
                players[match[0]] = {'w': 1, 'l': 0}

            if match[1] in players:
                players[match[1]]['l'] += 1
            else:
                players[match[1]] = {'l': 1, 'w': 0}

        zero_loss = []
        one_loss = []
        # print(players)
        for key, value in players.items():
            if value['l'] == 0:
                zero_loss.append(key)
            if value['l'] == 1:
                one_loss.append(key)
        return [sorted(zero_loss), sorted(one_loss)]