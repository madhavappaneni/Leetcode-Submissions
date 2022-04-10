class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)
        even = []
        evenIndices = []
        oddIndices = []
        odd = []
        s = ""
        for i, val in enumerate(num):
            if int(val) % 2 == 0:
                even.append(val)
                evenIndices.append(i)
            else:
                odd.append(val)
                oddIndices.append(i)
        even = sorted(even, reverse=True)
        odd = sorted(odd, reverse=True)
        # print(even, odd)
        # print(evenIndices, oddIndices)
        s = ["-"] * len(num)
        for i, val in enumerate(evenIndices):
            s[val] = even[i]
        for i, val in enumerate(oddIndices):
            s[val] = odd[i]
        return "".join(s)