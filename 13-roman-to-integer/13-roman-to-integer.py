class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) < 1 or len(s) > 15:
            print("The number is out of range")
            return 0
        
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if s in dict:
            return dict[s]
        
        sum = dict[s[0]]
        prev = s[0]
        
        for n in s[1:]:
            if dict[n] <= dict[prev]:
                sum += dict[n]
            elif dict[n] > dict[prev]:
                sum -= (2*dict[prev] - dict[n])
            prev = n
        return sum