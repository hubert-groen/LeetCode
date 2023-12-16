class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        counter = 0
        last_word = False
        
        for i in range(len(s)-1, -1, -1):
            
            if s[i] != ' ':
                counter += 1
                last_word = True

            elif (s[i] == ' ') and last_word is True:
                return counter
            
        return counter