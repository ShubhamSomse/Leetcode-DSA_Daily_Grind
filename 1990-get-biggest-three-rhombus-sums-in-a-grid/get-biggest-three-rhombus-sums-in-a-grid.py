class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = set()

        for i in range(m):
            for j in range(n):

                # radius = 0
                res.add(grid[i][j])

                k = 1
                while True:
                    if i-k < 0 or i+k >= m or j-k < 0 or j+k >= n:
                        break

                    s = 0

                    # top -> right
                    x, y = i-k, j
                    for t in range(k):
                        s += grid[x+t][y+t]

                    # right -> bottom
                    x, y = i, j+k
                    for t in range(k):
                        s += grid[x+t][y-t]

                    # bottom -> left
                    x, y = i+k, j
                    for t in range(k):
                        s += grid[x-t][y-t]

                    # left -> top
                    x, y = i, j-k
                    for t in range(k):
                        s += grid[x-t][y+t]

                    res.add(s)
                    k += 1

        return sorted(res, reverse=True)[:3]