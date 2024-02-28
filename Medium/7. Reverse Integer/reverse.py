class Solution:
    def reverse(self, x: int) -> int:
        string_x = str(x)
        neg = False
        if string_x[0] == '-':
            neg = True
            string_x = string_x[-1:0:-1]
        else:
            string_x = string_x[::-1]
        new_x = int(string_x)
        if new_x >= 2**31:
            new_x = 0
        elif neg:
            new_x = new_x *-1
        return new_x

print(Solution().reverse(-10))