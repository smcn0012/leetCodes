class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        out = ''
        if numRows == 1 or len(s) < numRows:
             return s
        zig_zag_len = (numRows - 1) * 2
        for zig_zag_num in range((len(s) - 1) // zig_zag_len + 1):
                out = out + s[zig_zag_num * zig_zag_len]

        for pair_num in range(numRows - 2):
            num_of_zig_zags = (len(s) - (pair_num + 2)) // zig_zag_len
            for zig_zag_num in range(num_of_zig_zags):
                out = out + s[pair_num + 1 + zig_zag_num * zig_zag_len]
                out = out + s[zig_zag_len - pair_num - 1 + zig_zag_num * zig_zag_len]
            out = out + s[pair_num + 1 + num_of_zig_zags * zig_zag_len]
            if ((len(s) - (zig_zag_len - pair_num)) // zig_zag_len) == num_of_zig_zags:
                 out = out + s[zig_zag_len - pair_num - 1 + num_of_zig_zags * zig_zag_len]

        for zig_zag_num in range((len(s) - numRows) // zig_zag_len + 1):
                out = out + s[numRows - 1 + zig_zag_num * zig_zag_len]
        return out
    
Solution().convert("PAYPALISHIRING", 4)