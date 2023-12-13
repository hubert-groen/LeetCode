class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        
        def fib(n):
        
            if n <=1:
                return 1

            elif n not in memo:
                memo[n] = fib(n-1) + fib(n-2)
                
            return memo[n]
        
        return fib(n)
