class Solution:
    def minimizeResult(self, expression: str) -> str:
        a, b = expression.split('+')
        # print(a, b)
        minVal = 100000000000
        ret_i, ret_j = 0, 0
        for i in range(0, len(a)):
            for j in range(1, len(b)+1):
                # print(i, j)
                val = ((int(a[:i] or 1) * (int(a[i:]) +
                       int(b[:j])) * int(b[j:] or '1')))
                if minVal >= val:
                    minVal = val
                    ret_i, ret_j = i, j
        return a[:ret_i] + "(" + a[ret_i:] + "+" + b[:ret_j] + ")" + b[ret_j:]
