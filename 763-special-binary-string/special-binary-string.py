class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        res = []
        count = 0
        start = 0
        
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1
            
            # found a special substring
            if count == 0:
                # recursively solve inner part
                inner = self.makeLargestSpecial(s[start+1:i])
                res.append('1' + inner + '0')
                start = i + 1
        
        # sort descending for lexicographically largest
        res.sort(reverse=True)
        
        return ''.join(res)