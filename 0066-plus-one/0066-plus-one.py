class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits)-1
        digits[i] += 1
        
        while digits[i] == 10 and i>0:
            digits[i-1] += 1
            digits[i] = 0
            i -= 1

        if digits[i] == 10:
            digits[i] = 0
            digits = [1] + digits

        return digits
