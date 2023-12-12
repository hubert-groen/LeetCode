class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        output = ''

        c = int(a, 2) + int(b, 2)
        
        if c == 0:
            output = str(0)

        while c > 0:
            
            output = str(c%2) + output
            c = c//2
        
        return output