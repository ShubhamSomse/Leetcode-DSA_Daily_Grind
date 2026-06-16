class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Convert the integer to a string
        str_n = str(n)
        
        # Reverse the string
        reversed_str_n = str_n[::-1]
        
        # Convert the reversed string back to an integer
        reversed_n = int(reversed_str_n)
        
        # Calculate the absolute difference
        mirror_dist = abs(n - reversed_n)
        
        return mirror_dist