class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def helper(suffix, i, j):
            if len(suffix) == 0:
                return True
            
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != suffix[0]:
                return False
            board[i][j] = '#'
            ans = helper(suffix[1:], i + 1, j) \
                or helper(suffix[1:], i, j + 1) \
                or helper(suffix[1:], i - 1, j) \
                or helper(suffix[1:], i, j - 1)

            board[i][j] = suffix[0]
            return ans


        for row in range(len(board)):
            for col in range(len(board[0])):
                if helper(word, row, col):
                    return True
        return False
            
            