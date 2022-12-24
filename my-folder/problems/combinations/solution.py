class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []

        def helper(first, curr):
            if len(curr) == k:
                out.append(curr[:])
            else:
                for idx in range(first, n + 1):
                    curr.append(idx)
                    helper(idx + 1, curr)
                    curr.pop()
        helper(1, [])
        return out
