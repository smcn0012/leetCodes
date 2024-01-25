class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_palindrome = 1
        longest_palindrome_index = 0
        for start_index, char in enumerate(s):
            if len(s) - start_index < longest_palindrome:
                    break
            for end_index in range(len(s) - 1, start_index, -1):
                if end_index - start_index + 1 < longest_palindrome:
                    break
                search = 0
                while s[end_index - search] == s[start_index + search]:
                    search += 1
                    if search > (end_index - start_index + 1) // 2:
                        if end_index - start_index + 1 > longest_palindrome:
                             longest_palindrome = end_index - start_index + 1
                             longest_palindrome_index = start_index
                        break
        return s[longest_palindrome_index:longest_palindrome_index + longest_palindrome]
        
print(Solution().longestPalindrome("aacabdkacaa"))
