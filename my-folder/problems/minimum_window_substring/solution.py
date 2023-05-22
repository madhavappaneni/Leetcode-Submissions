class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""

        l = 0
        minLen = float('inf')
        dict_t = Counter(t)
        curr_dict = defaultdict(int)
        ans = None, None

        want = len(dict_t)
        have = 0
        for r in range(len(s)):
            curr_dict[s[r]] += 1
            if s[r] in dict_t and curr_dict[s[r]] == dict_t[s[r]]:
                have += 1
            while have == want:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    ans = l, r
                curr_dict[s[l]] -= 1
                if s[l] in dict_t and curr_dict[s[l]] < dict_t[s[l]]:
                    have -= 1
                l += 1

        return s[ans[0]: ans[1] + 1] if minLen != float('inf') else ""