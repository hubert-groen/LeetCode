class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def check_word(first_index):

            for j in range(len(needle)):
                if needle[j] != haystack[first_index + j]:
                    return False

            return True
        
        for i in range(len(haystack)-len(needle)+1):

            if haystack[i] == needle[0]:
                if check_word(i) is True:
                    return i
                
        return -1
