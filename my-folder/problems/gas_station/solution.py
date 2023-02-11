class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # minIndex = 0
        # totalGas = 0
        # minGas = float('inf')
        # for i in range(len(gas)):
        #     totalGas += gas[i] - cost[i]
        #     if totalGas < minGas:
        #         minIndex = i
        #         minGas = totalGas
        # return (minIndex + 1) % len(gas) if totalGas >= 0 else -1

        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start