class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        plus1, i1 = num1.index('+'), num1.index('i')
        plus2, i2 = num2.index('+'), num2.index('i')
        a, b, c, d = int(num1[:plus1]), int(num1[plus1 + 1:i1]), int(num2[:plus2]), int(num2[plus2 + 1: i2])
        
        real = a * c - b * d 
        img = a * d + b * c

        return str(real) + '+' + str(img) + 'i'