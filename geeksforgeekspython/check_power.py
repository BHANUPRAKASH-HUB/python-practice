class Solution:
    def isPowerOfAnother(self, x, y):
        # Special case
        if x == 1:
            return y == 1
        
        # Keep dividing y by x
        while y % x == 0:
            y //= x
        
        return y == 1
