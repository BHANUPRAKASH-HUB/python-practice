class Solution:
    def sumOfSquares(self, number):
        return number * (number + 1) * (2 * number + 1) // 6
#other
"""
class Solution:
    def sumOfSquares(self, number):
        total = 0
        for i in range(1, number + 1):
            total += i * i
        return total




"""