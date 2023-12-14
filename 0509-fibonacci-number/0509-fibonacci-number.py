class Solution:
    
    memo = {}
    
    def fib(self, n: int) -> int:
        
        
        if n <= 1:
            return n
        
        elif n not in self.memo:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
            
            return self.memo[n]
            
        return self.memo[n]