class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        br_map = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        for br in s:
            if br in ['[', '(', '{']:
                stack.append(br)
            else:
                if stack:
                    e = stack.pop()
                    if br not in br_map or br_map[br] != e:
                        return False
                else:
                    return False

        return True if len(stack) == 0 else False