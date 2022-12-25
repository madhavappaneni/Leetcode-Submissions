class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(s):
            return s == s[::-1]
        
        out = []
        def helper(start, curr):
            if curr and not isPalindrome(curr[-1]):
                return
            if start == len(s):
                # print(start, curr)
                out.append(curr[:])
            for i in range(start, len(s)):
                curr.append(s[start:i + 1])
                helper(i + 1, curr)
                curr.pop()
        # print(out)
        helper(0, [])
        return out
            
