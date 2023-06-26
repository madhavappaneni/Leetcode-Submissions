class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        # @lru_cache(None)
        # def helper(idx):
        #     try:
        #         if idx >= len(questions):
        #             return 0
                
        #         return max(questions[i + 1][0] + helper(questions[i + 1][1] + i + 1) for i in range(idx, len(questions) - 1))
        #     except:
        #         return 0      
        # return helper(-1)


            #         if i >= len(q):
            #     return 0

            # return max(
            #     solve(i + 1),                    # skip
            #     solve(i + q[i][1] + 1) + q[i][0] # solve
            # )

        @lru_cache(None)
        def helper(idx):
            if idx >= len(questions):
                return 0
            return max(helper(idx + 1), questions[idx][0] + helper(idx + questions[idx][1] + 1))
                   
        return helper(0)

