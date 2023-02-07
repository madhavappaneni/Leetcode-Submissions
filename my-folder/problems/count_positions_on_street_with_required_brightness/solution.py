class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        
        rangeSum = [0] * (len(requirement) + 1)
        for pos, rng in lights:
            rangeSum[max(0, pos - rng)] += 1 
            rangeSum[min(n - 1, pos + rng) + 1] -= 1
        return sum(cnt>=req for cnt, req in zip(accumulate(rangeSum), requirement))
        
        # # print(requirement)
        # # print(rangeSum)
        # count = 1 if rangeSum[0] >= requirement[0] else 0
        # for i in range(1, len(requirement)):
        #     rangeSum[i] += rangeSum[i-1]
        #     if rangeSum[i] >= requirement[i]:
        #         count += 1
        
        # print(rangeSum)
        # return count


        
    

