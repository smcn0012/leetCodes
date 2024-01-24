class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_instance = [-1 for _ in range(ord('~') - ord(' ') + 1)]
        substring_start = 0
        longest_substring = 0
        for s_index, char in enumerate(s):
            char_index = ord(char) - ord(' ')
            if last_instance[char_index] >= substring_start:
                if s_index - substring_start > longest_substring:
                    longest_substring = s_index - substring_start
                substring_start = last_instance[char_index] + 1
            last_instance[char_index] = s_index
        if len(s) - substring_start > longest_substring:
            longest_substring = len(s) - substring_start

        return longest_substring
