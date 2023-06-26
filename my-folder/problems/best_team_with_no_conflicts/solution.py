class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        

        sorted_scores = [x for _,x in sorted(zip(ages,scores))]
        
        # @lru_cache(None)
        # def helper(prevScore, idx):
        #     if idx == len(ages):
        #         return 0
            
        #     currScore = sorted_scores[idx]

        #     if prevScore > currScore:
        #         return helper(prevScore, idx + 1)

        #     else:
        #         return max(
        #             helper(currScore, idx + 1) + currScore,
        #             helper(prevScore, idx + 1)
        #         )
        
        # return helper(-1, 0)

        @lru_cache(None)
        def helper(idx):
            if idx == len(sorted_scores):
                return 0
            maxValue = 0
            for i in range(idx + 1, len(scores)):
                if sorted_scores[i] >= sorted_scores[idx]:
                    maxValue = max(maxValue, helper(i))
            return maxValue + sorted_scores[idx]

        return max(helper(i) for i in range(len(scores)))









            