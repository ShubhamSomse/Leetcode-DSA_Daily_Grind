import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        def canFinish(T):
            total = 0
            for t in workerTimes:
                val = (2*T) // t
                x = int((math.sqrt(1 + 4*val) - 1) // 2)
                total += x
                if total >= mountainHeight:
                    return True
            return False
        
        l, r = 0, 10**18
        
        while l < r:
            mid = (l + r) // 2
            if canFinish(mid):
                r = mid
            else:
                l = mid + 1
        
        return l