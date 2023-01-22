class Solution:
    def convertToBase7(self, num: int) -> str:
        out = []
        sign = '-' if num < 0 else ""
        num = abs(num)
        if num == 0:
            return "0"
        while num > 0:
            num, rem = divmod(num, 7)
            out.append(rem)
        if sign == "-":
            return (sign)+''.join([str(i) for i in out[::-1]])
        else:
            return ''.join([str(i) for i in out[::-1]])
            