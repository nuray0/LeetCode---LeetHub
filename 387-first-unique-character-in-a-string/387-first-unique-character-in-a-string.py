 
class Solution:
    def firstUniqChar(self, s: str) -> int:
                      
        count = collections.Counter(s)
        
#        for i in range(len(s)):
#            if count[s[i]] == 1:
#                return i
            
        for index, char in enumerate(s):
            if count[char] == 1:
                return index
                
        return -1
    
    