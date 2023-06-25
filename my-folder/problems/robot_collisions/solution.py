class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        a = [[0] * 4 for _ in range(n)]
        for i in range(n):
            a[i][0] = positions[i]
            a[i][1] = healths[i]
            if directions[i] == 'L':
                a[i][2] = 0
            else:
                a[i][2] = 1
            a[i][3] = i

        a.sort(key=lambda x: x[0])
        stk = []
        for i in range(n):
            if a[i][2] == 0:
                is_valid = True
                while stk and a[stk[-1]][2] == 1 and is_valid:
                    idx = stk[-1]
                    if a[idx][1] < a[i][1]:
                        stk.pop()
                        a[i][1] -= 1
                    elif a[idx][1] == a[i][1]:
                        is_valid = False
                        stk.pop()
                    else:
                        is_valid = False
                        a[idx][1] -= 1
                if is_valid:
                    stk.append(i)
            else:
                stk.append(i)

        ans = []
        s1 = [[0] * 2 for _ in range(len(stk))]
        for i in range(len(stk)):
            idx = stk.pop()
            s1[i][0] = a[idx][1]
            s1[i][1] = a[idx][3]

        s1.sort(key=lambda x: x[1])
        for i in range(len(s1)):
            ans.append(s1[i][0])

        return ans