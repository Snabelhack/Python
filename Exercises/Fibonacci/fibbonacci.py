# fibonacci.py
class Fibonacci:
    # Initialize the Fibonacci object
    def __init__(self):
        # Cache the two base cases
        self.cache = [0, 1]
        
    def __call__(self, n):
        # Validate value of n, raise exception if not valid.
        if not(isinstance(n, int) or n >= 0):
            raise ValueError(f'Expected postive integer, input was "{n}"')
            
        # Check cache for previously calculated numbers
        if n < len(self.cache):
            return self.cache[n]
        
        # Else compute and append new number in Fib series
        else: 
            fib = self(n - 1) + self(n - 2)
            self.cache.append(fib)
        return self.cache[n]