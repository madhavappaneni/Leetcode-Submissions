class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # @lru_cache(None)
        # def helper(level, idx):
        #     if level == len(triangle):
        #         return 0
        #     return triangle[level][idx] + min(helper(level + 1, idx), helper(level + 1, idx + 1))
        
        # return helper(0, 0)

        for i in range(1, len(triangle)):
            prev = triangle[i - 1]
            curr = triangle[i]

            for j in range(len(curr)):
                first, second = float('inf'), float('inf')
                if 0 <= j - 1 < len(prev):
                    first = prev[j - 1]
                if 0 <= j < len(prev):
                    second = prev[j]
                curr[j] += min(first, second)
        return min(triangle[-1])