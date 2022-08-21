class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        dArray = [0] * (len(s) + 1)
        dArray[0] = ord(s[0])
        
        for i in range(1, len(s)):
            dArray[i] = ord(s[i]) - ord(s[i-1])
        
        for shift in shifts:
            start, end, direction = shift
            dArray[start] += (1 if direction == 1 else -1)
            dArray[end + 1] += (-1 if direction == 1 else 1)
        out = []
        c = 0
        for i in range(len(s)):
            c += dArray[i]
            pos = c
            while pos > 122: pos -= 26
            while pos < 97: pos += 26
            out.append(chr(pos))
        # print(out)
        return ''.join(out)