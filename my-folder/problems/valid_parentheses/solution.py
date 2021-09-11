from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        deq = deque()
        bracket_map = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        opening_brackets = bracket_map.keys()
        if(len(s) == 1): 
            return False
        for i in range(len(s)):
            element = s[i]
            if element in opening_brackets:
                deq.append(element)
            else:
                if deq:
                    removed_element = deq.pop()
                    if (bracket_map[removed_element] != s[i]):
                        return False
                else:
                    return False
        if deq:
            return False
        return True
