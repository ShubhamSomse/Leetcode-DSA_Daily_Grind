class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        
        diff1 = diff2 = 0
        res = float('inf')
        left = 0
        
        for right in range(len(s)):
            
            if int(s[right]) != right % 2:
                diff1 += 1
            if int(s[right]) != (1 - right % 2):
                diff2 += 1
            
            if right - left + 1 > n:
                if int(s[left]) != left % 2:
                    diff1 -= 1
                if int(s[left]) != (1 - left % 2):
                    diff2 -= 1
                left += 1
            
            if right - left + 1 == n:
                res = min(res, diff1, diff2)
        
        return res