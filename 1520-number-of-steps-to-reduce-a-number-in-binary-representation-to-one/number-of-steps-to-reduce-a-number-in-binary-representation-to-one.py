class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # traverse from right to left (ignore first bit for now)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            
            if bit + carry == 1:
                # odd → +1 then /2
                steps += 2
                carry = 1
            else:
                # even → only /2
                steps += 1
        
        return steps + carry