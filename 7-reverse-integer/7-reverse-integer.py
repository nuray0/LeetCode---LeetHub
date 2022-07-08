class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        a=1
        if x<0:
            a = -1
            x = -x
        while(x>0):
            reverse = (reverse*10) + x % 10 
            x = int(x/10)
        if reverse <= -2**31 or reverse >= 2**31-1:
            reverse = 0
        return a*reverse