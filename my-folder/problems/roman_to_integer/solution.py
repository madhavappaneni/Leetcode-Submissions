class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
        }
        sum = 0
        counter = 0
        while counter < len(s):
            if counter < len(s) -1 and s[counter] + s[counter+1] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                sum = sum + dict[s[counter] + s[counter+1]]
                counter = counter + 2
            else:    
                sum = sum + dict[s[counter]]
                counter = counter + 1
        return sum
