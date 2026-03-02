class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        
        # Step 1: count trailing zeros
        tz = []
        for row in grid:
            count = 0
            for x in reversed(row):
                if x == 0:
                    count += 1
                else:
                    break
            tz.append(count)
        
        swaps = 0
        
        # Step 2: greedy row placement
        for i in range(n):
            required = n - 1 - i
            j = i
            
            while j < n and tz[j] < required:
                j += 1
            
            if j == n:
                return -1
            
            # bubble up
            while j > i:
                tz[j], tz[j-1] = tz[j-1], tz[j]
                swaps += 1
                j -= 1
        
        return swaps