class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_instance = [-1 for _ in range(ord('~') - ord(' '))]
        substring_start = 0
        longest_substring = -1
        for s_index, char in enumerate(s):
            char_index = ord(char) - ord(' ')
            if last_instance[char_index] != -1:
                if s_index - substring_start > longest_substring:
                    longest_substring = s_index - substring_start
                substring_start = last_instance[char_index] + 1
                last_instance[char_index] = s_index
            last_instance[char_index] = s_index
        if longest_substring == -1:
            longest_substring = len(s)

        return longest_substring


Solution().lengthOfLongestSubstring(' ')