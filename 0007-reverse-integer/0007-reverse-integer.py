class Solution:
    def reverse(self, x: int) -> int:
        
        answer = ''
        negative = False
        if x < 0:
            negative = True
        elif x == 0:
            return 0
        x = str(abs(x))
        zero = False

        for i in reversed(x):
            if x == '0' and zero == False:
                continue

            zero = True
            answer += i

        answer = int(answer)
        if negative == True:
            answer = answer * -1
        if abs(answer) > 2147483647:
            return 0

        return answer