class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        bit_len = 0
        
        for i in range(1, n + 1):
            # If i is a power of two → bit-length increases
            if (i & (i - 1)) == 0:
                bit_len += 1
            
            ans = ((ans << bit_len) + i) % MOD
        
        return ans