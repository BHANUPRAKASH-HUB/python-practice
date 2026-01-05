class Solution:
    def closestNumber(self, n, m):
        lower = (n // m) * m
        upper = lower + m

        if abs(n - lower) < abs(n - upper):
            return lower
        elif abs(n - lower) > abs(n - upper):
            return upper
        else:
            return lower if abs(lower) > abs(upper) else upper
