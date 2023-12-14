class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        
        def fib(n):
        
            # if n <=1:         # to też pasuje
            #     return 1      # ale poniższe bardziej intuicyjne
            
            if n <= 2:
                return n

            elif n not in memo:
                memo[n] = fib(n-1) + fib(n-2)
                
            return memo[n]
        
        return fib(n)
