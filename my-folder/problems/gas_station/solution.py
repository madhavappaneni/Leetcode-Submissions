class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasRemaining = 0
        minGas = float("inf")
        minGasIndex = 0
        for i in range(len(gas)):
            gasRemaining += gas[i] - cost[i]
            if gasRemaining < minGas:
                minGas = gasRemaining
                minGasIndex = i
            # print(gasRemaining)
        return (minGasIndex + 1) % len(gas) if gasRemaining >= 0 else -1
            
        