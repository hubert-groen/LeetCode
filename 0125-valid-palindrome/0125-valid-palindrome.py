class Solution:
    def isPalindrome(self, s: str) -> bool:

        def ascii(char):
            
            return 'A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9'


        start_pointer = 0
        end_pointer = len(s) - 1


        while start_pointer < end_pointer:

            if not ascii(s[start_pointer]):
                start_pointer += 1
                continue

            if not ascii(s[end_pointer]):
                end_pointer -= 1
                continue

            ss = s[start_pointer]
            es = s[end_pointer]

            if s[start_pointer].lower() != s[end_pointer].lower() :
                return False
            
            start_pointer += 1
            end_pointer -= 1

            if start_pointer > end_pointer:
                return True

        if start_pointer > end_pointer:
            return False
            
        return True    