class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p, q = p / 2, q / 2
            
        if p % 2==0 and q % 2==1: #if p even and q odd
            return 2
        
        elif p % 2==1 and q % 2==0: #if p odd and q even
            return 0
        
        else:                   #if p odd and q odd
            return 1
        