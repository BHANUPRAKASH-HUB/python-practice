class Solution:
    def pairCubeCount(self, n):
        count = 0
        
        # Precompute cubes for speed
        cubes = set()
        i = 0
        while i**3 <= n:
            cubes.add(i**3)
            i += 1
        
        a = 1
        while a**3 <= n:
            remaining = n - a**3
            if remaining in cubes:
                count += 1
            a += 1
        
        return count
