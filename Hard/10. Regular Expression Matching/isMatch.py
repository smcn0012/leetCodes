class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        string_index = 0
        previous_char = ''
        for p_index, char in enumerate(p):
            if char == '.':
                string_index += 1
            elif char == '*':
                if previous_char == '.':
                    if p_index + 1 >= len(p):
                        return True
                    else:
                        index_of_non_wild = p_index + 1
                        while p[p_index + 1] == '.' or p[p_index + 1] == '*':
                            index_of_non_wild += 1
                        while s[string_index] != p[index_of_non_wild]:
                            string_index += 1
                            if string_index >= len(s):
                                break
                else:
                    while s[string_index] == previous_char:
                        string_index += 1
                        if string_index >= len(s):
                            
                            break
            else:
                if char == s[string_index]:
                    string_index += 1
                elif p_index + 1 > len(p) or p[p_index + 1] != '*':
                    return False
            previous_char = char
            if string_index >= len(s):
                return True
        return False

