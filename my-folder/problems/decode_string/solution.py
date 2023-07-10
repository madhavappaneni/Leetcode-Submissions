class Solution:
    def decodeString(self, s: str) -> str:

        out = []

        for ch in s:
            if ch != ']':
                out.append(ch)
            else:
                word = []
                while out[-1] != '[':
                    word.append(out.pop())
                out.pop()
                count = []

                while out and out[-1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    count.append(out.pop())
                
                out.extend(word[::-1] * int(''.join(count[::-1])))
        
        return ''.join(out)