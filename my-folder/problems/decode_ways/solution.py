class Solution:
    def numDecodings(self, s: str) -> int:
        mem = [0] * (len(s) + 1)
        mem[0] = 1
        mem[1] = 0 if s[0] == "0" else 1
        
        for i in range(2, len(mem)):
            if s[i - 1] != "0":
                mem[i] = mem[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                mem[i] += mem[i - 2]
        print(mem)
        return mem[len(s)]
        
        # mem = [-1] * (len(s) + 1)
#         def helper(idx):
#             if mem[idx] != -1:
#                 return mem[idx]
            
#             if idx == len(s):
#                 mem[idx] = 1
#                 return mem[idx]
            
#             if s[idx] == "0":
#                 mem[idx] = 0
#                 return mem[idx]     
            
#             if idx == len(s) - 1:
#                 return 1
            
#             first = helper(idx + 1)
#             second = helper(idx + 2) if int(s[idx:idx+2]) <= 26 else 0
#             mem[idx] = first + second
#             return mem[idx]
#         return helper(0)
    

