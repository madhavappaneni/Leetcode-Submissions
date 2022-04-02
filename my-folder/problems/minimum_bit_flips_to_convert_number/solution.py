class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        goal_str_len = len(str(bin(goal))[2:])
        start_str_len = len(str(bin(start)[2:]))
        start_str = "0" * (goal_str_len - start_str_len) + str(bin(start)
                                                               [2:]) if goal_str_len > start_str_len else str(bin(start)[2:])
        goal_str = "0" * (start_str_len - goal_str_len) + str(bin(goal)
                                                              [2:]) if start_str_len > goal_str_len else str(bin(goal)[2:])

        count = 0
        for i in range(len(start_str)):
            if start_str[i] != goal_str[i]:
                count += 1
        return (count)    
