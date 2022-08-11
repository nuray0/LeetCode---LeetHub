class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        i = 0
        while i < rowIndex:
            res.append(1)
            for j in range(len(res)-2,0, -1):
                res[j] += res[j-1]
            i+=1
            
        return res
            
            
        