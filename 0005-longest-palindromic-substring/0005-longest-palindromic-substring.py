class Solution:
    def longestPalindrome(self, s: str) -> str:

        total_record = 1
        start_index = 0
    
        def check_THREE(p1, p2):
            curr_rec = 3

            while p1 != 0 and p2 != len(s)-1:
                p1 -= 1
                p2 += 1

                if s[p1] == s[p2]:
                    curr_rec += 2
                else:
                    return curr_rec, p1+1
                
            return curr_rec, p1

        def check_TWO(p1, p2):
            curr_rec = 2

            while p1 != 0 and p2 != len(s)-1:
                p1 -= 1 
                p2 += 1

                if s[p1] == s[p2]:
                    curr_rec += 2
                else:
                    return curr_rec, p1+1

            return curr_rec, p1


        for i in range(0, len(s)- 2):


            if s[i] == s[i+2]:
                # print(f"i = {i} and we make check_THREE")
                rec, r1 = check_THREE(i, i+2)

                # print(f"rec = {rec}")
                # print('\n')

                if rec > total_record:
                    total_record = rec
                    start_index = r1
            
            if s[i+1] == s[i+2]:
                # print(f"i = {i} and we make check_TWO")
                rec, r1 = check_TWO(i+1, i+2)

                # print(f"rec = {rec}")
                # print('\n')

                if rec > total_record:
                    total_record = rec
                    start_index = r1

        if len(s) > 1 and total_record == 1 and s[0] == s[1]:
            total_record = 2

        output = s[start_index : start_index + total_record]
        return output