class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1: return False
    
        stack = []
        brackets = {'(':')', '{':'}', '[':']'}
        
        for i in s:
            if i in brackets:
                stack.append(i)
            elif len(stack) == 0 or brackets[stack.pop()] != i:
                return False
            
        return len(stack) == 0
    
        # replacing closed brackets with empty string
#        while len(s) > 0:
#            l = len(s)
#            s = s.replace('()','').replace('{}','').replace('[]','')
#            if l==len(s): return False
#        return True