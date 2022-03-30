class Solution:
    def fib(self, n: int) -> int:
        
        fib = [0] * (n + 1)
        
        def fib_helper(n):
            if n == 0 or n == 1:
                fib[n] = n
                return n 
            else: 
                if fib[n-1] == 0:
                    fib[n-1] = fib_helper(n-1)
                fib_1 = fib[n-1]

                if fib[n-2] == 0:
                    fib[n-2] = fib_helper(n-2)
                fib_2 = fib[n-2]

                return fib_1 + fib_2
        return fib_helper(n)