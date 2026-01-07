class Solution:
    def doOverlap(self, L1, R1, L2, R2):
        # If one rectangle is on left side of other
        if L1[0] > R2[0] or L2[0] > R1[0]:
            return 0

        # If one rectangle is above other
        if R1[1] > L2[1] or R2[1] > L1[1]:
            return 0

        return 1
