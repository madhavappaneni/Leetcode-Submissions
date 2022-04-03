class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_mins = int(current[:2]) * 60 + int(current[3:])
        correct_mins = int(correct[:2]) * 60 + int(correct[3:])
        diff = correct_mins - current_mins
        count = 0
        while diff > 0:
            if diff // 60 > 0:
                count += diff // 60
                diff = diff % 60
            if diff // 15 > 0:
                count += diff // 15
                diff = diff % 15
            if diff // 5 > 0:
                count += diff // 5
                diff = diff % 5
            if diff // 1 > 0:
                count += diff // 1
                diff = diff % 1

        return count