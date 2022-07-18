class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        
        if m < 1 or m > 100 or n < 1 or n > 100:
            raise ValueError("invalid value for either m or n")
            
        if r < 1 or r > 300 or c < 1 or c > 300:
            raise ValueError("invalid value for either r or c")
        
        if m * n != r * c:
            return mat   
        elif m == r and n == c:
            return mat
        

        output = []
        
#        # nested loop method - copy each element
#        for i in range(m):
#            for j in range(n):
#                if len(output[-1]) < c:
#                    output[-1].append(mat[i][j])
#                else:
#                    output.append([mat[i][j]])
    
    
        # list comprehension method - flatten and copy
        flat = [element for subset in mat for element in subset]
        
        for i in range(r):
            output.append(flat[i * c : (i + 1) * c])
            
        return output
            
                    
        