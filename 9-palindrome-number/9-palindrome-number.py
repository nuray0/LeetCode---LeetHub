class Solution:
    def isPalindrome(self, x: int):
        if x<0 or (x%10 == 0 and x != 0):
            return False
        elif x == 0:
            return True
        elif x > 2**31-1 or x < -2**31:
            return False
        reverse = 0
        while (x > reverse):
            reverse = reverse*10 + x%10
            x = int(x/10)
        return x == reverse or x == int(reverse/10)
            
        