class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        
        bits = num.bit_length()
        mask = (1 << bits) - 1
        return num ^ mask