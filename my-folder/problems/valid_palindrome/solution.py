class Solution:
    def isPalindrome(self, s: str) -> bool:

        start, end = 0, len(s) - 1


        while start < end:

            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue

            cond = (s[start] == s[end] or s[start].lower() == s[end].lower())
            if (cond):
                start += 1
                end -= 1
            else:
                return False

        return True