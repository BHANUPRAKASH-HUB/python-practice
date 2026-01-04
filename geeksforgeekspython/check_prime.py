class Solution:
    def isPrime(self, n):
        # 1 and numbers less than 1 are not prime
        if n <= 1:
            return False
        
        # 2 and 3 are prime
        if n <= 3:
            return True
        
        # eliminate even numbers
        if n % 2 == 0:
            return False
        
        # check divisibility up to sqrt(n)
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        
        return True
