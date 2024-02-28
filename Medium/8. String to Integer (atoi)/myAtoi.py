class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        s_index = 0
        number = '0'
        while s[s_index] == ' ':
            s_index += 1
            if s_index >= len(s):
                return 0
        sign = 1
        if s[s_index] == '-':
            if len(s) != 1:
                sign = -1
                s_index += 1
            else:
                return 0
        elif s[s_index] == '+':
            if len(s) != 1:
                s_index += 1
            else:
                return 0
        
        while ord(s[s_index]) <= 57 and ord(s[s_index]) >= 48:
            number = number + (s[s_index])
            s_index += 1
            if s_index >= len(s):
                break
        
        number = int(number)
        if number >= 2**31:
            if sign == -1:
                return -(2**31)
            return 2**31 - 1
        else:
            return number * sign