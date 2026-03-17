class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    heights[c] = 0
                else:
                    heights[c] += 1

            sorted_heights = sorted(heights, reverse=True)

            for i in range(n):
                ans = max(ans, sorted_heights[i] * (i + 1))

        return ans