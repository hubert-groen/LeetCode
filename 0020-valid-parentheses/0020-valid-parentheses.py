class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        d = {')': '(', ']': '[', '}': '{'}

        stack = []

        for i in s:
            if i not in d:
                stack.append(i)
            else:
                if len(stack) != 0 and d[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False