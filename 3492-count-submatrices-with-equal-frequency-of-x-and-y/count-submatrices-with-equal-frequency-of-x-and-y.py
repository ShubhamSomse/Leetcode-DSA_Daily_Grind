class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        prefix_sum = [[0]*(n+1) for _ in range(m+1)]
        prefix_x = [[0]*(n+1) for _ in range(m+1)]
        
        res = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                val = 0
                if grid[i-1][j-1] == 'X':
                    val = 1
                elif grid[i-1][j-1] == 'Y':
                    val = -1
                
                # build prefix sum
                prefix_sum[i][j] = (
                    val
                    + prefix_sum[i-1][j]
                    + prefix_sum[i][j-1]
                    - prefix_sum[i-1][j-1]
                )
                
                # count X
                prefix_x[i][j] = (
                    (1 if grid[i-1][j-1] == 'X' else 0)
                    + prefix_x[i-1][j]
                    + prefix_x[i][j-1]
                    - prefix_x[i-1][j-1]
                )
                
                # check condition
                if prefix_sum[i][j] == 0 and prefix_x[i][j] > 0:
                    res += 1
        
        return res