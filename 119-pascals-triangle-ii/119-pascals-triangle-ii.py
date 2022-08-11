class Solution():    
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        if rowIndex == 0: return [1]
        ans = self.getRow(rowIndex - 1)
        return [1] + [sum(x) for x in zip(ans, ans[1:])] + [1]

                
            
            
        