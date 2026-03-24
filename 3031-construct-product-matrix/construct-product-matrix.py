class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        
        n, m = len(grid), len(grid[0])
        arr = []
        
        # flatten
        for row in grid:
            arr.extend(row)
        
        size = len(arr)
        res = [1] * size
        
        # prefix
        prefix = 1
        for i in range(size):
            res[i] = prefix
            prefix = (prefix * arr[i]) % MOD
        
        # suffix
        suffix = 1
        for i in range(size - 1, -1, -1):
            res[i] = (res[i] * suffix) % MOD
            suffix = (suffix * arr[i]) % MOD
        
        # reshape to 2D
        ans = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(res[idx])
                idx += 1
            ans.append(row)
        
        return ans