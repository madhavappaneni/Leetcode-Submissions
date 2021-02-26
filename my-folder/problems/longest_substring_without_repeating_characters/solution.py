class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = []
        max_count = 0
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in uniq:
                    count = count + 1
                    uniq.append(s[j])
                else:
                    if (count > max_count):
                        max_count = count 
                    uniq = []
                    count = 0
                    break
            if(count > max_count):
                max_count = count
        return max_count