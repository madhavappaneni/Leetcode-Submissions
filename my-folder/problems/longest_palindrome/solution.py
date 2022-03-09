class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashMap = {}
        
        for i in s:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
            
        ans = 0
        for i in hashMap:
            ans += hashMap[i] // 2 * 2
            if ans % 2 == 0 and hashMap[i] % 2 == 1:
                ans += 1
        return ans