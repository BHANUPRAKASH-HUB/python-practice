class Solution:
    def lcm(self, a, b):
        # Compute GCD using Euclidean Algorithm
        x, y = a, b
        while y != 0:
            x, y = y, x % y
        
        gcd = x
        
        # LCM formula
        return (a * b) // gcd
