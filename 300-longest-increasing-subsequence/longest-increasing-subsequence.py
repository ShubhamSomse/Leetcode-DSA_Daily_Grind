class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0

        for x in nums:
            i, j = 0, size
            while i < j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            if i == size:
                size += 1

        return size

        #Greedy + Binary Search (Patience Sorting Technique)

# Used to solve:

# 👉 300 Longest Increasing Subsequence
# in O(n log n) time instead of O(n²).
