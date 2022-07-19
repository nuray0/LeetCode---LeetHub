class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        index = {}
        for i in range(len(s)):
            index[s[i]] = i
            
        list_chars = [char for char in s]
                      
        count = collections.Counter(list_chars)
        
        min_index = len(s)
        
        for char, number in count.items():
            if number == 1 and index[char] < min_index:
                min_index = index[char]
                
        return min_index if min_index < len(s) else -1
