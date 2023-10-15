class Solution:
    def romanToInt(self, s: str) -> int:

        s = s + 'N'

        rules = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'N': 0}

        output = 0
        skip = False

        for i in range(len(s) - 1):

            if skip == True:
                skip = False
                continue

            if rules[s[i]] >= rules[s[i+1]] or i+1 == len(s):
                output += rules[s[i]]
            else:
                output += (rules[s[i+1]] - rules[s[i]])
                skip = True

        return output